"""
LILIETH Kernel — Core Algorithms
=================================
Five foundational algorithms that power the Sovereign OS:

  1. S.U.E. (Sovereign Unified Equation) Validator — ethical gate for .ai commands
  2. Indra-Vajra Kinetic Harvester           — converts physical motion to Sovereign Joules
  3. OUSH Handshake                          — P2P finality / block-lock signature check
  4. Enki-Flow Constant (Φ_mersey)           — hydraulic power potential of the Mersey Corridor
  5. Social ROI (ROI_soc)                    — deletion-of-poverty return on hydraulic investment
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
# 4.  Enki-Flow Constant  (Φ_mersey — Hydraulic Power Potential)
# ---------------------------------------------------------------------------

def calculate_enki_flow(
    eta: float,
    rho: float,
    g: float,
    Q: float,
    delta_h: float,
) -> float:
    """Calculate the Enki-Flow Constant (Φ_mersey) for the Mersey Corridor.

    Formula
    -------
    ``Φ_mersey = η · ρ · g · Q · Δh``

    where:

    * ``η``       — Lemniscate (Figure-of-Eight) turbine efficiency [0, 1].
                    Traditional turbines ≈ 0.60; Lemniscate turbines ≈ 0.94.
    * ``ρ``       — Density of Mersey H₂O in kg/m³.  Brackish water enriched with
                    reclaimed Oceanic Copper particulates exceeds 1000 kg/m³.
    * ``g``       — Gravitational acceleration in m/s² (standard: 9.81).
    * ``Q``       — Sub-surface laminar flow rate in m³/s.  The Venturi Effect
                    created by Lip-Turbines accelerates Q without a dam.
    * ``Δh``      — Sovereign Head: vertical drop across the turbine stage in
                    metres.  Even 1 m, multiplied by river mass, exceeds the
                    torque of a thousand static diesel generators.

    Parameters
    ----------
    eta:
        Turbine efficiency coefficient (0.0 – 1.0).
    rho:
        Water density in kg/m³.
    g:
        Gravitational acceleration in m/s².
    Q:
        Volumetric flow rate in m³/s.
    delta_h:
        Hydraulic head (vertical drop) in metres.

    Returns
    -------
    float
        Sovereign Watts generated by the Enki-Node.  Always ≥ 0.
    """
    phi = eta * rho * g * Q * delta_h
    return max(0.0, phi)


# ---------------------------------------------------------------------------
# 5.  Social ROI  (ROI_soc — Deletion-of-Poverty Return)
# ---------------------------------------------------------------------------

_SOCIAL_ROI_GUARD = 1e-9  # prevents division-by-zero when outputs are zero


def calculate_social_roi(
    V_pure: float,
    psi_pow: float,
    sigma_time: float,
    S_sloth: float,
    delta_bill: float,
) -> float:
    """Calculate the Social Return on Investment (ROI_soc) of the Enki-Flow system.

    Formula
    -------
    ``ROI_soc = (S_sloth + Δ_bill) / ((V_pure + Ψ_pow) · Σ_time)``

    Interpretation: ROI_soc measures how many units of *eliminated burden*
    (administrative waste + utility bills) are unlocked per unit of *sovereign
    output* (free water × free power × reclaimed human hours).  A score > 1.0
    means the system is returning more value than the static cost it displaces —
    the "Deletion of Poverty" threshold.

    Parameters
    ----------
    V_pure:
        Volume of free, high-pressure, filtered water delivered to the community
        (47,000 residents), in litres per day.
    psi_pow:
        Sovereign Wattage generated by the Enki-Nodes (Ψ_pow).
    sigma_time:
        Human hours reclaimed per day when residents no longer pay water/power
        bills (Σ_time).
    S_sloth:
        Estimated daily cost of the Water Board's administrative friction (£).
    delta_bill:
        Total daily cost of utility bills eliminated by the Enki-Flow system (£).

    Returns
    -------
    float
        ROI_soc index.  Values > 1.0 confirm the "Social Surplus" — the system
        is generating more sovereign value than it displaces in static cost.
    """
    numerator = S_sloth + delta_bill
    denominator = (V_pure + psi_pow) * sigma_time
    return numerator / (denominator + _SOCIAL_ROI_GUARD)
