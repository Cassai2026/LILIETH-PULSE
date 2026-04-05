"""
LILIETH Kernel — Core Algorithms
=================================
Five foundational algorithms that power the Sovereign OS:

  1. S.U.E. (Sovereign Unified Equation) Validator — ethical gate for .ai commands
  2. Indra-Vajra Kinetic Harvester           — converts physical motion to Sovereign Joules
  3. OUSH Handshake                          — P2P finality / block-lock signature check
  4. Tectonic-Tread Constant (Φ_seis)        — piezoelectric harvest from kinetic slabs
  5. Biological ROI (ROI_bio)                — return on human body movement / vitality
"""

from __future__ import annotations

from typing import Dict, List


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
# 4.  Tectonic-Tread Constant  (Φ_seis)
# ---------------------------------------------------------------------------

def calculate_tectonic_tread_constant(
    masses: List[float],
    displacements: List[float],
    frequencies: List[float],
    piezo_coefficient: float,
    g: float = 9.81,
) -> float:
    """Calculate the Tectonic-Tread Constant (Φ_seis).

    Sums the piezoelectric energy contribution of every mass-impact event
    across the Sovereign Kinetic Slab array (e.g. the A56 corridor).

    Formula
    -------
    ``Φ_seis = Σ_i (m_i · g · h_i · f_i · ζ)``

    where:

    * ``m_i``  = mass of each impact source in kg
                 (range: ~80 kg human step → 44,000 kg HGV)
    * ``g``    = gravitational acceleration (default 9.81 m/s²)
    * ``h_i``  = slab compression displacement in metres
                 (4D-printed slabs allow 0.002–0.005 m deflection)
    * ``f_i``  = frequency of impacts per day for each source
                 (A56 sees 20,000–40,000 vehicles/day × 4 wheels)
    * ``ζ``    = Piezo-Conversion Coefficient — mechanical-to-electrical
                 efficiency of the Oceanic Copper / ceramic crystal matrix

    Parameters
    ----------
    masses:
        List of impact masses ``m_i`` in kilograms.
    displacements:
        List of slab compression displacements ``h_i`` in metres.
        Must have the same length as *masses*.
    frequencies:
        List of daily impact frequencies ``f_i`` for each source.
        Must have the same length as *masses*.
    piezo_coefficient:
        The dimensionless Piezo-Conversion Coefficient ``ζ``.
    g:
        Gravitational acceleration in m/s².  Defaults to 9.81.

    Returns
    -------
    float
        Total harvestable energy in Sovereign Joules (always ≥ 0).

    Raises
    ------
    ValueError
        If *masses*, *displacements*, and *frequencies* are not all the
        same length, or if any list is empty.
    """
    if not masses:
        raise ValueError(
            "calculate_tectonic_tread_constant: masses list must not be empty."
        )
    if not (len(masses) == len(displacements) == len(frequencies)):
        raise ValueError(
            "calculate_tectonic_tread_constant: masses, displacements, and "
            "frequencies must all have the same length."
        )

    phi_seis = sum(
        m * g * h * f * piezo_coefficient
        for m, h, f in zip(masses, displacements, frequencies)
    )
    return max(0.0, phi_seis)


# ---------------------------------------------------------------------------
# 5.  Biological ROI  (ROI_bio)
# ---------------------------------------------------------------------------

def calculate_biological_roi(
    b_pulse: float,
    steps: float,
    induction_multiplier: float,
    delta_tox: float,
    s_sedentary: float,
) -> float:
    """Calculate the Biological Return on Investment (ROI_bio).

    Quantifies the sovereign energy yield of a resident's daily movement
    against the drag imposed by pollution and sedentary behaviour.

    Formula
    -------
    ``ROI_bio = (B_pulse · ΣSteps · μ) / (Δ_tox + S_sedentary)``

    where:

    * ``B_pulse``  = biometric vitality score of the resident [0.0, 1.0]
    * ``ΣSteps``   = total daily step count (30,000-step mandate)
    * ``μ``        = Induction Multiplier — heel-strike capture efficiency
                     of the Sovereign Shoes
    * ``Δ_tox``    = toxic drag coefficient from A56 pollution
                     (neutralised by Co2WorX interventions)
    * ``S_sedentary`` = static cost of sedentary behaviour (the "Rinse")

    The tiny constant ``0.0004`` guards against division-by-zero when both
    drag terms are zero (fully sovereign, zero-pollution baseline).

    Parameters
    ----------
    b_pulse:
        Biometric vitality score ``B_pulse`` in the range [0.0, 1.0].
    steps:
        Total daily step count ``ΣSteps``.
    induction_multiplier:
        Sovereign Shoe heel-strike efficiency ``μ`` (0.0–1.0).
    delta_tox:
        Pollution drag coefficient ``Δ_tox`` (≥ 0).
    s_sedentary:
        Sedentary behaviour cost ``S_sedentary`` (≥ 0).

    Returns
    -------
    float
        ROI_bio index.  A value **> 1.0** indicates that the resident's
        kinetic output outweighs environmental and behavioural drag —
        *Harvested Equity* confirmed.
    """
    _STATIC_GUARD = 0.0004  # prevents division-by-zero when drag terms are both 0

    numerator = b_pulse * steps * induction_multiplier
    denominator = delta_tox + s_sedentary + _STATIC_GUARD
    return numerator / denominator
