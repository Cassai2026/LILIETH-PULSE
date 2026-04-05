"""
LILIETH Kernel — Extensible Parser (The Python Foundry)
========================================================
Parses four custom LILIETH file types into structured AST-like dictionaries:

  .v   (Vajra)   — Logic / Induction math commands
  .kg  (KONG)    — Physical execution / Material integrity commands
  .4d  (Eternius)— Spatial / Temporal blueprints
  .ai  (Animus)  — Ethical governance / 14+1 Pillars commands

Token syntax
------------
Each non-blank, non-comment line must follow the **abc12345** pattern::

    <action><balance><connection><scale><dimension><spirit>[<args>...]

Where the *header token* is 6+ alphanumeric characters:

  * **a** — Action  (what to do)
  * **b** — Balance  (equilibrium qualifier)
  * **c** — Connection (mesh link)
  * **1** — Scale  (numeric dimension 1)
  * **2** — Scale  (numeric dimension 2)
  * **3** — Scale  (numeric dimension 3)
  * **4** — Scale  (numeric dimension 4)
  * **5** — Spirit  (final sovereign intent)

Lines starting with ``#`` are treated as comments and skipped.

The `.ai` interpreter gates all ``give`` commands through the S.U.E. validator.
The `.kg` interpreter listens for ``take`` commands and triggers the Indra-Vajra
kinetic harvester.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from core.algorithms import (
    calculate_phi_fire,
    calculate_roi_env,
    calculate_sue_score,
    harvest_kinetic_energy,
    oush_handshake,
)


# ---------------------------------------------------------------------------
# Token / Node types
# ---------------------------------------------------------------------------

TOKEN_PATTERN = re.compile(
    r"^(?P<action>[a-zA-Z]+)"       # Action  — one or more letters
    r"(?P<scale>[0-9]+)"            # Scale   — one or more digits
    r"(?P<args>.*)$"                # Args    — remainder of line (optional)
)

# Minimal "abc12345" token requires at least 3 letters + 5 digits.
# Used to validate tokens in strict-mode extensions (.ai, .v).
ABC12345_PATTERN = re.compile(r"^[a-zA-Z]{3,}[0-9]{5,}")

# Extensions that require the strict abc12345 minimum token format.
_STRICT_EXTENSIONS: frozenset[str] = frozenset({".ai", ".v"})


class ParseError(Exception):
    """Raised when a LILIETH source file contains a syntax error."""


class ASTNode:
    """A single parsed instruction node."""

    __slots__ = ("file_type", "action", "scale", "args", "raw", "line_no")

    def __init__(
        self,
        file_type: str,
        action: str,
        scale: str,
        args: str,
        raw: str,
        line_no: int,
    ) -> None:
        self.file_type = file_type
        self.action = action.lower()
        self.scale = scale
        self.args = args.strip()
        self.raw = raw
        self.line_no = line_no

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file_type": self.file_type,
            "action": self.action,
            "scale": self.scale,
            "args": self.args,
            "raw": self.raw,
            "line_no": self.line_no,
        }

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"ASTNode(type={self.file_type!r}, action={self.action!r}, "
            f"scale={self.scale!r}, args={self.args!r}, line={self.line_no})"
        )


# ---------------------------------------------------------------------------
# Base interpreter
# ---------------------------------------------------------------------------

class BaseInterpreter:
    """Base class for per-extension interpreters.

    Sub-classes override :meth:`execute_node` to provide type-specific
    behaviour and can register *hook* callbacks for specific actions.
    """

    extension: str = ""  # must be set by sub-class, e.g. ".v"

    def __init__(self) -> None:
        self._hooks: Dict[str, List[Callable[[ASTNode], Any]]] = {}

    # ------------------------------------------------------------------
    # Hook registration
    # ------------------------------------------------------------------

    def register_hook(self, action: str, callback: Callable[[ASTNode], Any]) -> None:
        """Register *callback* to be called whenever *action* is encountered."""
        self._hooks.setdefault(action.lower(), []).append(callback)

    def _fire_hooks(self, node: ASTNode) -> None:
        for cb in self._hooks.get(node.action, []):
            cb(node)

    # ------------------------------------------------------------------
    # Execution entry-point
    # ------------------------------------------------------------------

    def execute(self, nodes: List[ASTNode]) -> List[Any]:
        """Execute a list of AST nodes and return their results."""
        results = []
        for node in nodes:
            result = self.execute_node(node)
            self._fire_hooks(node)
            results.append(result)
        return results

    def execute_node(self, node: ASTNode) -> Any:  # pragma: no cover
        """Override in sub-classes."""
        return node.to_dict()


# ---------------------------------------------------------------------------
# Specialised interpreters
# ---------------------------------------------------------------------------

class VajraInterpreter(BaseInterpreter):
    """Interpreter for .v (Vajra) — Logic / Induction math."""

    extension = ".v"

    def execute_node(self, node: ASTNode) -> Dict[str, Any]:
        result = node.to_dict()
        result["vajra_induction"] = f"logic_pulse:{node.action}@scale={node.scale}"
        return result


class KongInterpreter(BaseInterpreter):
    """Interpreter for .kg (KONG) — Physical execution / Material integrity.

    Automatically triggers the Indra-Vajra kinetic harvester whenever a
    ``take`` command is parsed from a `.v` source file (injected via hook).

    Section IV — Phlogiston Protocol commands:

    * ``dissociate`` — plasma gasification; triggers :func:`~core.algorithms.calculate_phi_fire`
    * ``sequester``  — carbon sequestration; triggers :func:`~core.algorithms.calculate_roi_env`
    """

    extension = ".kg"

    def __init__(self) -> None:
        super().__init__()
        # Default kinetic-harvester parameters; callers may override.
        self._traffic_density: float = 1.0
        self._velocity_avg: float = 1.0
        # Default Φ_fire parameters (Phlogiston Thermal Induction).
        self._phi_fire_params: Dict[str, float] = {
            "m_waste": 47000.0,   # kg — input from 47,000 residents
            "delta_tox": 0.01,    # near-zero toxicity coefficient for plasma
            "q_plasma": 5.0,      # MJ/kg plasma heat flux
            "delta_t": 4800.0,    # K thermal differential (5000°C kiln core)
            "e_ash_sum": 2350.0,  # kg mineral equity of Bio-Active Ash
        }
        # Default ROI_env parameters (Environmental ROI).
        self._roi_env_params: Dict[str, float] = {
            "carbon_seq": 1200.0,      # tonnes — 100 Ash Trees + vitrified slag
            "soil_vit": 850.0,         # soil vitality index from E_ash
            "growth_multiplier": 5.0,  # Λ — Sovereign Forest accelerated rate
            "landfill_vol": 94000.0,   # m³ static waste removed
            "emission_stat": 3100.0,   # tCO₂e baseline displaced
        }

    def set_kinetic_params(self, traffic_density: float, velocity_avg: float) -> None:
        """Configure the kinetic harvester parameters used on 'take' commands."""
        self._traffic_density = traffic_density
        self._velocity_avg = velocity_avg

    def set_phi_fire_params(
        self,
        m_waste: float,
        delta_tox: float,
        q_plasma: float,
        delta_t: float,
        e_ash_sum: float,
    ) -> None:
        """Configure the Φ_fire plasma gasification parameters for 'dissociate' commands."""
        self._phi_fire_params = {
            "m_waste": m_waste,
            "delta_tox": delta_tox,
            "q_plasma": q_plasma,
            "delta_t": delta_t,
            "e_ash_sum": e_ash_sum,
        }

    def set_roi_env_params(
        self,
        carbon_seq: float,
        soil_vit: float,
        growth_multiplier: float,
        landfill_vol: float,
        emission_stat: float,
    ) -> None:
        """Configure the ROI_env parameters for 'sequester' commands."""
        self._roi_env_params = {
            "carbon_seq": carbon_seq,
            "soil_vit": soil_vit,
            "growth_multiplier": growth_multiplier,
            "landfill_vol": landfill_vol,
            "emission_stat": emission_stat,
        }

    def execute_node(self, node: ASTNode) -> Dict[str, Any]:
        result = node.to_dict()
        if node.action == "take":
            joules = harvest_kinetic_energy(self._traffic_density, self._velocity_avg)
            result["sovereign_joules"] = joules
            result["kong_status"] = f"kinetic_harvest:{joules:.4f}J"
        elif node.action == "dissociate":
            phi = calculate_phi_fire(**self._phi_fire_params)
            result["phi_fire"] = phi
            result["kong_status"] = f"plasma_dissociation:phi_fire={phi:.6f}"
        elif node.action == "sequester":
            roi = calculate_roi_env(**self._roi_env_params)
            result["roi_env"] = roi
            result["kong_status"] = f"carbon_sequestration:roi_env={roi:.6f}"
        else:
            result["kong_status"] = f"material_integrity:{node.action}@{node.scale}"
        return result

    def handle_vajra_take(self, node: ASTNode) -> None:
        """Hook target: called when a 'take' command appears in a .v file."""
        joules = harvest_kinetic_energy(self._traffic_density, self._velocity_avg)
        print(
            f"[KONG] Vajra 'take' detected (line {node.line_no}). "
            f"Kinetic harvest triggered → {joules:.4f} Sovereign Joules."
        )


class EterniusInterpreter(BaseInterpreter):
    """Interpreter for .4d (Eternius) — Spatial / Temporal blueprints."""

    extension = ".4d"

    def execute_node(self, node: ASTNode) -> Dict[str, Any]:
        result = node.to_dict()
        result["eternius_blueprint"] = f"spatial_temporal:{node.action}@{node.scale}D"
        # Trigger OUSH finality on 'lock' commands.
        if node.action == "lock":
            node_id = node.args if node.args else f"eternius_{node.line_no}"
            locked = oush_handshake(node_id, "ARCHITECT_ALPHA")
            result["oush_locked"] = locked
        return result


class AnimusInterpreter(BaseInterpreter):
    """Interpreter for .ai (Animus) — Ethical governance / 14+1 Pillars.

    All ``give`` commands are gated by the S.U.E. validator before execution.
    The default virtue/sin profiles can be replaced via :meth:`set_ethical_profile`.
    """

    extension = ".ai"

    _DEFAULT_VIRTUES: Dict[str, float] = {
        "love": 0.9,
        "truth": 0.85,
        "courage": 0.8,
        "wisdom": 0.88,
        "justice": 0.82,
        "temperance": 0.75,
        "sovereignty": 0.95,
    }

    _DEFAULT_SINS: Dict[str, float] = {
        "greed": 0.1,
        "sloth": 0.05,
        "wrath": 0.08,
        "envy": 0.06,
        "pride": 0.07,
        "gluttony": 0.04,
        "lust": 0.03,
    }

    def __init__(self) -> None:
        super().__init__()
        self._virtues = dict(self._DEFAULT_VIRTUES)
        self._sins = dict(self._DEFAULT_SINS)

    def set_ethical_profile(
        self,
        virtues: Dict[str, float],
        sins: Dict[str, float],
    ) -> None:
        """Override the default 7-virtue / 7-sin ethical profile."""
        self._virtues = dict(virtues)
        self._sins = dict(sins)

    def execute_node(self, node: ASTNode) -> Dict[str, Any]:
        result = node.to_dict()
        if node.action == "give":
            sue_score = calculate_sue_score(self._virtues, self._sins)
            result["sue_score"] = sue_score
            if sue_score > 1.0:
                result["animus_status"] = "GIVE_PERMITTED"
                result["pillar_gate"] = "PULSE_CONFIRMED"
            else:
                result["animus_status"] = "GIVE_BLOCKED"
                result["pillar_gate"] = "STATIC_SLOTH"
        else:
            result["animus_status"] = f"pillar_exec:{node.action}@{node.scale}"
        return result


# ---------------------------------------------------------------------------
# Main Parser (The Foundry)
# ---------------------------------------------------------------------------

class LiliethParser:
    """Extensible parser for LILIETH sovereign OS source files.

    Supported extensions out-of-the-box:

    * ``.v``   — Vajra (logic / induction math)
    * ``.kg``  — KONG (physical execution / material integrity)
    * ``.4d``  — Eternius (spatial / temporal blueprints)
    * ``.ai``  — Animus (ethical governance / 14+1 Pillars)

    Additional interpreters can be registered at runtime via
    :meth:`register_interpreter`.

    Usage
    -----
    ::

        parser = LiliethParser()
        nodes  = parser.parse_file("protocols/lilieth_core.ai")
        result = parser.execute(nodes)
    """

    def __init__(self) -> None:
        self._interpreters: Dict[str, BaseInterpreter] = {}
        self._register_defaults()

    # ------------------------------------------------------------------
    # Default interpreter registration
    # ------------------------------------------------------------------

    def _register_defaults(self) -> None:
        vajra = VajraInterpreter()
        kong = KongInterpreter()
        eternius = EterniusInterpreter()
        animus = AnimusInterpreter()

        # Wire up the KONG listener: fires whenever a Vajra 'take' is hit.
        vajra.register_hook("take", kong.handle_vajra_take)

        for interp in (vajra, kong, eternius, animus):
            self.register_interpreter(interp)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def register_interpreter(self, interpreter: BaseInterpreter) -> None:
        """Register a custom interpreter for a file extension.

        Parameters
        ----------
        interpreter:
            An instance of a :class:`BaseInterpreter` sub-class.  Its
            ``extension`` attribute (e.g. ``".v"``) is used as the key.
        """
        ext = interpreter.extension.lower()
        if not ext.startswith("."):
            ext = f".{ext}"
        self._interpreters[ext] = interpreter

    def get_interpreter(self, extension: str) -> Optional[BaseInterpreter]:
        """Return the interpreter registered for *extension*, or ``None``."""
        ext = extension.lower()
        if not ext.startswith("."):
            ext = f".{ext}"
        return self._interpreters.get(ext)

    def parse_source(
        self,
        source: str,
        file_type: str,
    ) -> List[ASTNode]:
        """Parse *source* text as the given *file_type* extension.

        Parameters
        ----------
        source:
            Raw text content of the file.
        file_type:
            Extension string, e.g. ``".ai"`` or ``"ai"``.

        Returns
        -------
        list of ASTNode
        """
        ext = file_type.lower()
        if not ext.startswith("."):
            ext = f".{ext}"

        nodes: List[ASTNode] = []
        for line_no, raw_line in enumerate(source.splitlines(), start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            match = TOKEN_PATTERN.match(line)
            if not match:
                raise ParseError(
                    f"[{ext}:{line_no}] Invalid token syntax: {raw_line!r}\n"
                    "  Expected format: <action-letters><scale-digits>[<args>]"
                )

            action = match.group("action")
            scale = match.group("scale")
            args = match.group("args")

            # Enforce the full abc12345 format (≥3 letters + ≥5 digits) for
            # strict extensions (.ai governance commands and .v induction math).
            if ext in _STRICT_EXTENSIONS and not ABC12345_PATTERN.match(line):
                raise ParseError(
                    f"[{ext}:{line_no}] Token does not meet abc12345 format "
                    f"(≥3 action letters + ≥5 scale digits): {raw_line!r}"
                )

            nodes.append(
                ASTNode(
                    file_type=ext,
                    action=action,
                    scale=scale,
                    args=args,
                    raw=raw_line,
                    line_no=line_no,
                )
            )
        return nodes

    def parse_file(self, path: str | Path) -> List[ASTNode]:
        """Parse the file at *path* and return a list of :class:`ASTNode` objects.

        The file extension is used automatically to select the correct interpreter.
        """
        p = Path(path)
        source = p.read_text(encoding="utf-8")
        return self.parse_source(source, p.suffix)

    def execute(
        self,
        nodes: List[ASTNode],
        file_type: Optional[str] = None,
    ) -> List[Any]:
        """Execute *nodes* using the appropriate interpreter.

        Parameters
        ----------
        nodes:
            A list of :class:`ASTNode` instances (all must share the same
            ``file_type``, or *file_type* must be supplied explicitly).
        file_type:
            Override the extension used to look up the interpreter.  When
            omitted, the ``file_type`` of the first node is used.

        Returns
        -------
        list
            One result dict per node.
        """
        if not nodes:
            return []

        ext = file_type or nodes[0].file_type
        interpreter = self.get_interpreter(ext)
        if interpreter is None:
            raise ParseError(f"No interpreter registered for extension: {ext!r}")
        return interpreter.execute(nodes)

    def parse_and_execute(self, path: str | Path) -> List[Any]:
        """Convenience method: parse *path* and immediately execute it."""
        nodes = self.parse_file(path)
        return self.execute(nodes)
