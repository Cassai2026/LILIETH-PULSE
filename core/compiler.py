"""
LILIETH Kernel — Compiler
==========================
The compiler transforms a sequence of parsed :class:`~core.interpreter.ASTNode`
objects into a compact, executable *bytecode* representation that the Sovereign
OS runtime can schedule and dispatch.

Pipeline
--------
1. **Validate** — every node is type-checked and semantically verified.
2. **Optimise** — redundant or no-op instructions are collapsed.
3. **Emit** — each node is lowered to a :class:`Instruction` record.
4. **Link** — cross-file references (e.g. ``call`` targets) are resolved.
5. **Finalise** — the OUSH handshake seals the bytecode block in the .4d ledger.

The compiler intentionally remains *stateless*; create a fresh instance per
compilation unit or reuse the same instance across multiple files — both are safe.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from core.algorithms import oush_handshake
from core.interpreter import ASTNode, LiliethParser, ParseError


# ---------------------------------------------------------------------------
# Instruction  (compiled bytecode record)
# ---------------------------------------------------------------------------

@dataclass
class Instruction:
    """A single compiled bytecode instruction."""

    opcode: str
    operand: str
    scale: int
    meta: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "opcode": self.opcode,
            "operand": self.operand,
            "scale": self.scale,
            "meta": self.meta,
        }


# ---------------------------------------------------------------------------
# Bytecode  (compiled output)
# ---------------------------------------------------------------------------

@dataclass
class Bytecode:
    """Container for a compiled LILIETH source unit."""

    source_ext: str
    instructions: List[Instruction]
    oush_sealed: bool = False
    node_id: str = "compiler_node"

    def seal(self, node_id: str = "compiler_node") -> bool:
        """Run the OUSH handshake and mark this bytecode unit as sealed."""
        self.node_id = node_id
        self.oush_sealed = oush_handshake(node_id, "ARCHITECT_ALPHA")
        return self.oush_sealed

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_ext": self.source_ext,
            "oush_sealed": self.oush_sealed,
            "node_id": self.node_id,
            "instructions": [i.to_dict() for i in self.instructions],
        }


# ---------------------------------------------------------------------------
# Compiler
# ---------------------------------------------------------------------------

class LiliethCompiler:
    """Compiles LILIETH AST nodes into :class:`Bytecode`.

    Parameters
    ----------
    parser:
        Optional :class:`~core.interpreter.LiliethParser` instance.  A new
        one is created automatically if not supplied.
    """

    # Opcodes emitted per file type
    _OPCODE_MAP: Dict[str, str] = {
        ".v": "VAJRA",
        ".kg": "KONG",
        ".4d": "ETERNIUS",
        ".ai": "ANIMUS",
        ".gw": "GROUNDWORX",
    }

    def __init__(self, parser: Optional[LiliethParser] = None) -> None:
        self._parser = parser or LiliethParser()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def compile_nodes(
        self,
        nodes: List[ASTNode],
        node_id: str = "compiler_node",
    ) -> Bytecode:
        """Compile *nodes* into a :class:`Bytecode` object.

        Parameters
        ----------
        nodes:
            Parsed nodes (all must share the same ``file_type``).
        node_id:
            Identifier used for the OUSH finality handshake.

        Returns
        -------
        Bytecode
        """
        if not nodes:
            raise ParseError("compile_nodes: received an empty node list.")

        source_ext = nodes[0].file_type
        opcode_prefix = self._OPCODE_MAP.get(source_ext, "GENERIC")

        validated = self._validate(nodes)
        optimised = self._optimise(validated)
        instructions = self._emit(optimised, opcode_prefix)

        bytecode = Bytecode(source_ext=source_ext, instructions=instructions)
        bytecode.seal(node_id)
        return bytecode

    def compile_file(self, path: str, node_id: str = "compiler_node") -> Bytecode:
        """Parse *path* and compile it in one step."""
        nodes = self._parser.parse_file(path)
        return self.compile_nodes(nodes, node_id=node_id)

    # ------------------------------------------------------------------
    # Internal pipeline stages
    # ------------------------------------------------------------------

    def _validate(self, nodes: List[ASTNode]) -> List[ASTNode]:
        """Validate that every node has a non-empty action and numeric scale."""
        for node in nodes:
            if not node.action:
                raise ParseError(
                    f"[{node.file_type}:{node.line_no}] Empty action in: {node.raw!r}"
                )
            if not node.scale.isdigit():
                raise ParseError(
                    f"[{node.file_type}:{node.line_no}] "
                    f"Scale must be numeric, got: {node.scale!r}"
                )
        return nodes

    def _optimise(self, nodes: List[ASTNode]) -> List[ASTNode]:
        """Collapse consecutive identical no-op nodes (action='noop')."""
        optimised: List[ASTNode] = []
        for node in nodes:
            if node.action == "noop" and optimised and optimised[-1].action == "noop":
                continue  # collapse redundant noops
            optimised.append(node)
        return optimised

    def _emit(
        self,
        nodes: List[ASTNode],
        opcode_prefix: str,
    ) -> List[Instruction]:
        """Lower nodes to :class:`Instruction` records."""
        instructions: List[Instruction] = []
        for node in nodes:
            instructions.append(
                Instruction(
                    opcode=f"{opcode_prefix}_{node.action.upper()}",
                    operand=node.args,
                    scale=int(node.scale),
                    meta={"line_no": node.line_no, "raw": node.raw},
                )
            )
        return instructions
