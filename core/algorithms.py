"""
LILIETH Kernel — Core Algorithms
=================================
Five foundational algorithms that power the Sovereign OS:

  1. S.U.E. (Sovereign Unified Equation) Validator — ethical gate for .ai commands
  2. Indra-Vajra Kinetic Harvester           — converts physical motion to Sovereign Joules
  3. OUSH Handshake                          — P2P finality / block-lock signature check
  4. Φ_fire (Phlogiston Thermal Induction)   — plasma gasification mass-balance equation
  5. ROI_env (Environmental ROI)             — regeneration return on waste resources
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
# 4.  Φ_fire  (Phlogiston Thermal Induction Equation)
# ---------------------------------------------------------------------------

def calculate_phi_fire(
    m_waste: float,
    delta_tox: float,
    q_plasma: float,
    delta_t: float,
    e_ash_sum: float,
) -> float:
    """Calculate the Φ_fire plasma gasification thermal induction value.

    The Phlogiston Protocol treats Municipal Solid Waste as a Resource Deposit.
    High-voltage plasma dissociation rips complex molecular chains into elemental
    components (H₂, CO) and vitrified minerals (Bio-Active Ash, E_ash).

    Formula
    -------
    ``Φ_fire = (M_waste × δ_tox) / ((Q_plasma × ΔT) + Σ_E_ash)``

    where:

    * ``M_waste``    — input mass of waste in kilograms
    * ``δ_tox``      — toxicity reduction coefficient (approaches 0 for clean plasma)
    * ``Q_plasma``   — plasma heat flux (energy density for molecular dissociation)
    * ``ΔT``         — thermal differential between kiln core and heat exchangers
    * ``Σ_E_ash``    — summed mineral equity of Bio-Active Ash produced

    Parameters
    ----------
    m_waste:
        Input waste mass in kilograms (e.g. total from 47,000 residents).
    delta_tox:
        Toxicity coefficient in range [0.0, 1.0].  Plasma gasification drives
        this towards 0, meaning negligible residual complex toxins.
    q_plasma:
        Plasma heat flux in MJ/kg — energy density of the plasma torch.
    delta_t:
        Thermal differential in kelvin between the Vulcan Kiln core and the
        Sovereign Spine heat exchangers.
    e_ash_sum:
        Cumulative mineral equity (kg) of E_ash nutrient concentrate produced.

    Returns
    -------
    float
        Φ_fire value (dimensionless thermal-induction index).  Higher values
        indicate greater toxic-mass conversion per unit of thermal-mineral output.
        Always ≥ 0.

    Notes
    -----
    A tiny constant ``1e-9`` prevents division-by-zero when the denominator is 0.
    """
    _PLASMA_GUARD = 1e-9  # prevents division-by-zero

    numerator = m_waste * delta_tox
    denominator = (q_plasma * delta_t) + e_ash_sum + _PLASMA_GUARD
    return max(0.0, numerator / denominator)


# ---------------------------------------------------------------------------
# 5.  ROI_env  (Environmental Return on Investment)
# ---------------------------------------------------------------------------

def calculate_roi_env(
    carbon_seq: float,
    soil_vit: float,
    growth_multiplier: float,
    landfill_vol: float,
    emission_stat: float,
) -> float:
    """Calculate the Environmental ROI for the Stretford Meadows regeneration.

    Waste is reframed as a Resource Deposit: the cost of living drops while the
    quality of the environment rises.  This equation quantifies that trade-off.

    Formula
    -------
    ``ROI_env = ((Carbon_seq + Soil_vit) × Λ) / (Landfill_vol + Emission_stat)``

    where:

    * ``Carbon_seq``      — carbon locked into ash trees and vitrified slag (tonnes)
    * ``Soil_vit``        — increase in soil nutrient density from E_ash application
    * ``Λ``               — growth multiplier (accelerated biological rate)
    * ``Landfill_vol``    — volume of static waste removed from the Earth (m³)
    * ``Emission_stat``   — baseline emissions displaced by the plasma system (tCO₂e)

    Parameters
    ----------
    carbon_seq:
        Carbon sequestration in tonnes — amount locked into the 100 Ash Trees
        and the vitrified slag used by GroundWorX.
    soil_vit:
        Soil vitality index — increase in nutrient density from E_ash application.
    growth_multiplier:
        Λ, the Sovereign Forest accelerated biological rate (dimensionless scalar).
    landfill_vol:
        Volume of static waste (m³) removed from the Stretford Meadows.
    emission_stat:
        Baseline static-world emissions (tCO₂e) displaced by the Vulcan Kiln.

    Returns
    -------
    float
        ROI_env index.  A value **> 1.0** indicates net environmental gain
        (regeneration outweighs historical damage).  Always ≥ 0.

    Notes
    -----
    A tiny constant ``1e-9`` prevents division-by-zero when both ``landfill_vol``
    and ``emission_stat`` are zero.
    """
    _LANDFILL_GUARD = 1e-9  # prevents division-by-zero

    numerator = (carbon_seq + soil_vit) * growth_multiplier
    denominator = landfill_vol + emission_stat + _LANDFILL_GUARD
    return max(0.0, numerator / denominator)
