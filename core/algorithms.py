"""
LILIETH Kernel — Core Algorithms
=================================
Four foundational algorithms that power the Sovereign OS:

  1. S.U.E. (Sovereign Unified Equation) Validator — ethical gate for .ai commands
  2. Indra-Vajra Kinetic Harvester           — converts physical motion to Sovereign Joules
  3. OUSH Handshake                          — P2P finality / block-lock signature check
  4. Φ_alc (Alchemical Equation)             — Bio-Chemical ROI for the Ninkasi BrewWorX Pillar
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


# ---------------------------------------------------------------------------
# 4.  Φ_alc  (Alchemical Equation — Section X: Ninkasi BrewWorX Pillar)
# ---------------------------------------------------------------------------

def calculate_phi_alc(
    chemical_rinse: float,
    delta_rot: float,
    e_ash: float,
    enzymes: Dict[str, float],
) -> float:
    """Calculate the Alchemical Bio-Chemical ROI (Φ_alc) for the Ninkasi BrewWorX Pillar.

    Formula
    -------
    ``Φ_alc = (Chemical_Rinse + δ_rot) / (E_ash · ΣEnzymes)``

    where:

    * ``Chemical_Rinse`` — removal potency of old-world pesticides and synthetic
      "Static" fertilizers (range [0.0, 1.0]).
    * ``δ_rot``          — conversion coefficient of organic waste back into
      Life-Force (range [0.0, 1.0]).
    * ``E_ash``          — mineral concentrate harvested from the Section IV
      Vulcan Kilns (kg, ≥ 0).
    * ``ΣEnzymes``       — sum of biological "Spark" potencies produced when the
      Stretford Meadows flora is fermented with Sovereign H₂O.

    Parameters
    ----------
    chemical_rinse:
        Purification coefficient for removing Static pesticide residue.
    delta_rot:
        Organic-waste Life-Force conversion coefficient.
    e_ash:
        Mineral-concentrate mass from the Vulcan Kilns.
    enzymes:
        Dictionary mapping enzyme names to their potency scores (each in [0.0, 1.0]).

    Returns
    -------
    float
        Φ_alc index.  Higher values indicate richer Animus Fuel synthesis.
        A value **> 1.0** signals that the BrewWorX tonic exceeds the baseline
        Sovereign threshold.  Returns 0.0 when both inputs are zero.

    Notes
    -----
    The tiny constant ``0.0001`` prevents division-by-zero when ``e_ash`` or all
    enzyme potencies are 0.
    """
    _STATIC_GUARD = 0.0001  # prevents division-by-zero

    numerator = chemical_rinse + delta_rot
    enzyme_sum = sum(enzymes.values())
    denominator = (e_ash * enzyme_sum) + _STATIC_GUARD

    return numerator / denominator
