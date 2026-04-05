"""
LILIETH Kernel — Core Algorithms
=================================
Four foundational algorithms that power the Sovereign OS:

  1. S.U.E. (Sovereign Unified Equation) Validator — ethical gate for .ai commands
  2. Indra-Vajra Kinetic Harvester           — converts physical motion to Sovereign Joules
  3. OUSH Handshake                          — P2P finality / block-lock signature check
  4. Ω_bal (Omega Balance)                   — EquiWorX Social Stability (Section IX:
                                               The Pillar of Inanna)
"""

from __future__ import annotations

from typing import Dict


# ---------------------------------------------------------------------------
# 1.  S.U.E.  (Sovereign Unified Equation)
# ---------------------------------------------------------------------------

def calculate_sue_score(virtues: Dict[str, float], sins: Dict[str, float]) -> float:
    """Calculate the Sovereign Unified Equation (S.U.E.) score.

    Parameters
    ----------
    virtues:
        A dictionary of seven Lumen (virtue) scores, each in the range [0.0, 1.0].
        Expected keys (any seven virtue names are accepted):
        e.g. ``{'love': 0.9, 'truth': 0.8, ...}``
    sins:
        A dictionary of seven Umbra (sin) scores, each in the range [0.0, 1.0].

    Returns
    -------
    float
        S.U.E. index.  A score **> 1.0** indicates that virtues outweigh sins and
        the action is permitted (Pulse confirmed).  A score ≤ 1.0 means the action
        is blocked (Static Sloth condition).

    Notes
    -----
    The tiny constant ``0.0004`` prevents division-by-zero when all sin scores are 0.
    """
    _STATIC_SLOTH_GUARD = 0.0004  # prevents division-by-zero

    lumen_sum = sum(virtues.values())
    umbra_sum = sum(sins.values())

    sue_index = lumen_sum / (umbra_sum + _STATIC_SLOTH_GUARD)
    return sue_index


# ---------------------------------------------------------------------------
# 2.  Indra-Vajra Kinetic Harvester
# ---------------------------------------------------------------------------

def harvest_kinetic_energy(traffic_density: float, velocity_avg: float) -> float:
    """Convert road-traffic motion into Sovereign Joules via piezoelectric induction.

    Formula
    -------
    ``Phi = (Kmv * Mu) - Loss``

    where:

    * ``Kmv``  = kinetic mass-velocity  (``traffic_density × velocity_avg``)
    * ``Mu``   = reclaimed-copper efficiency coefficient (0.98)
    * ``Loss`` = system thermal/conversion loss (0.02)

    Parameters
    ----------
    traffic_density:
        Number of vehicles (or aggregate mass units) per unit length of slab.
    velocity_avg:
        Average velocity of traffic in metres per second.

    Returns
    -------
    float
        Sovereign Joules harvested.  Always ≥ 0 (negative energy is clamped to 0).
    """
    RECLAIMED_COPPER_MU = 0.98
    SYSTEM_LOSS = 0.02

    kinetic_mass = traffic_density * velocity_avg
    joules = (kinetic_mass * RECLAIMED_COPPER_MU) - SYSTEM_LOSS
    return max(0.0, joules)


# ---------------------------------------------------------------------------
# 3.  OUSH Handshake  (Finality / Block-Lock)
# ---------------------------------------------------------------------------

_VALID_SIGNATURE = "ARCHITECT_ALPHA"


# ---------------------------------------------------------------------------
# 4.  Ω_bal  (Omega Balance) — EquiWorX Social Stability Equation
#     Section IX: The Pillar of Inanna
# ---------------------------------------------------------------------------

#: Total nodes in the 21⁴ Sovereign Pyramid (21 ** 4 = 194 481)
SOVEREIGN_NODE_COUNT: int = 194_481

#: Ω_bal threshold below which the mesh is considered socially stable
OMEGA_BALANCE_STABLE_THRESHOLD: float = 1.0

#: Guard prevents division-by-zero when Ψ_sync or ΣHearts is 0
_OMEGA_ZERO_GUARD: float = 1e-9


def calculate_omega_bal(
    psi_sync: float,
    sum_hearts: float,
    delta_friction: float,
    s_sloth: float,
) -> float:
    """Calculate the EquiWorX Social Stability index (Ω_bal).

    The Pillar of Inanna — Dynamic Balance equation:

    .. math::

        \\Omega_{bal} = \\frac{(\\Delta_{friction} + S_{sloth})^2}{\\Psi_{sync}
        \\cdot \\sum Hearts}

    A **low** Ω_bal (< :data:`OMEGA_BALANCE_STABLE_THRESHOLD`) indicates that
    friction and sloth are small relative to collective synchronisation and
    biological output — the mesh is in Dynamic Balance.
    A **high** Ω_bal signals systemic instability requiring EquiWorX
    intervention.

    Parameters
    ----------
    psi_sync:
        Level of shared Induction across the four levels of the 21⁴ pyramid
        (Ψ_sync).  Expected range [0.0, 1.0].
    sum_hearts:
        Total biological output of the collective (ΣHearts).  Must be ≥ 0.
    delta_friction:
        Magnitude of static arguments or misunderstandings that the CareWorX
        psychologists must neutralise (Δ_friction).
    s_sloth:
        Delay factor in the 1:1:1 resource distribution cycle (S_sloth).

    Returns
    -------
    float
        Ω_bal index.  Values **< 1.0** indicate a stable mesh.
        Values **≥ 1.0** indicate an unstable mesh requiring rebalancing.
        Always ≥ 0 (negative results are clamped to 0).

    Raises
    ------
    ValueError
        If ``sum_hearts`` or ``psi_sync`` is negative.
    """
    if psi_sync < 0:
        raise ValueError("psi_sync must be non-negative")
    if sum_hearts < 0:
        raise ValueError("sum_hearts must be non-negative")

    numerator = (delta_friction + s_sloth) ** 2
    denominator = (psi_sync * sum_hearts) + _OMEGA_ZERO_GUARD

    omega = numerator / denominator
    return max(0.0, omega)


def oush_handshake(node_id: str, pulse_signature: str) -> bool:
    """Verify the P2P OUSH connection and lock a block in the .4d ledger.

    Parameters
    ----------
    node_id:
        Unique identifier of the requesting node.
    pulse_signature:
        Cryptographic-style pulse token supplied by the node.

    Returns
    -------
    bool
        ``True`` if the node is authenticated and sovereignty is locked;
        ``False`` otherwise.
    """
    if pulse_signature == _VALID_SIGNATURE:
        print(f"NODE {node_id}: SOVEREIGNTY LOCKED. OUSH.")
        return True
    print(f"NODE {node_id}: HANDSHAKE FAILED. SIGNATURE INVALID.")
    return False
