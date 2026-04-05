"""
LILIETH Kernel — Core Algorithms
=================================
Five foundational algorithms that power the Sovereign OS:

  1. S.U.E. (Sovereign Unified Equation) Validator — ethical gate for .ai commands
  2. Indra-Vajra Kinetic Harvester           — converts physical motion to Sovereign Joules
  3. OUSH Handshake                          — P2P finality / block-lock signature check
  4. Aetheric Induction Constant (Ψ_sync)   — mesh capacity of the Sovereign Aetheric relay
  5. Digital ROI Equation (ROI_dig)          — cognitive-freedom return on digital sovereignty
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


def calculate_aetheric_sync(
    b_width: float,
    kappa_ether: float,
    beth_kernel: float,
    delta_lag: float,
    sigma_noise: float,
) -> float:
    """Calculate the Aetheric Induction Constant (Ψ_sync) for the Sovereign Mesh.

    Ψ_sync expresses the ratio of residual latency-noise to available bandwidth
    and kernel capacity.  A **lower** Ψ_sync indicates a cleaner, higher-capacity
    channel (more bandwidth, purer kernel, less lag).  A **higher** Ψ_sync signals
    that noise and latency are dominant relative to the mesh's carrying capacity.

    Formula
    -------
    ``Ψ_sync = (δ_lag × σ_noise) / ((B_width × κ_ether) × ℶ_kernel)``

    Parameters
    ----------
    b_width:
        Aetheric Bandwidth — multi-dimensional data-layering capacity of the
        Dual-Tetrahedron node array (arbitrary Sovereign units).
    kappa_ether:
        Dielectric Permittivity — ionisation-derived data capacity of the
        atmospheric waveguide (arbitrary Sovereign units).
    beth_kernel:
        Kernel Integrity (ℶ_kernel) — purity of the LILIETH OS, expressed as a
        fraction in ``[0.0, 1.0]``.  A value of ``1.0`` denotes zero "Static" bloat
        and 100 % processing efficiency.
    delta_lag:
        Decision Latency (δ_lag) — round-trip signal latency of the mesh in
        nanoseconds.  Approaches zero for fully resident node clusters.
    sigma_noise:
        Noise coefficient (σ_noise) — residual interference from external
        "Static" sources; dimensionless.

    Returns
    -------
    float
        Ψ_sync index.  Always ≥ 0.  A value approaching **0** represents optimal
        mesh quality (minimal lag/noise, maximum bandwidth).  Returns 0 when the
        numerator is zero or the denominator would otherwise be zero (guarded by a
        small epsilon).

    Notes
    -----
    A small epsilon (``1e-12``) is applied to the denominator to prevent
    division-by-zero when any of *b_width*, *kappa_ether*, or *beth_kernel* is 0.
    """
    _EPSILON = 1e-12

    numerator = delta_lag * sigma_noise
    denominator = (b_width * kappa_ether) * beth_kernel

    if numerator == 0.0:
        return 0.0

    psi_sync = numerator / (denominator + _EPSILON)
    return max(0.0, psi_sync)


# ---------------------------------------------------------------------------
# 5.  Digital ROI Equation  (ROI_dig)
# ---------------------------------------------------------------------------

def calculate_digital_roi(
    autonomy_priv: float,
    equity_data: float,
    rinse_sum: float,
    s_sloth: float,
    phi_mersey: float,
) -> float:
    """Calculate the Digital Sovereignty Return on Investment (ROI_dig).

    ROI_dig measures the Cognitive Freedom unlocked by replacing centralised
    "Internet" infrastructure with the Sovereign Aetheric Mesh.  A higher value
    indicates greater liberation from "Rinse" friction.

    Formula
    -------
    ``ROI_dig = (∑Rinse + S_sloth) / ((Autonomy_priv + Equity_data) × Φ_mersey)``

    Parameters
    ----------
    autonomy_priv:
        Value of a private, sovereign communication network that external
        monopolies cannot track or throttle (Sovereign £ units).
    equity_data:
        Collective knowledge equity stored in the Abzu Ground-Nervous System
        (Sovereign £ units; e.g. £10 Octillion = ``1e28``).
    rinse_sum:
        Total friction removed — the sum of subscription fees, data-theft costs,
        and advertising overhead eliminated by the Sovereign Mesh (Sovereign £ units).
    s_sloth:
        Static Sloth coefficient drawn from the S.U.E. sin register; represents
        residual inertia within the legacy digital system (dimensionless, ≥ 0).
    phi_mersey:
        Mersey Sovereign Multiplier (Φ_mersey) — amplification factor derived
        from the community energy of the 47,000 residents (dimensionless, > 0).

    Returns
    -------
    float
        ROI_dig index.  Always ≥ 0.  Represents the ratio of legacy friction cost
        to the value of sovereign digital freedom.  A value approaching **0**
        means that Cognitive Freedom far outweighs residual "Rinse" friction
        (the equity denominator dominates).  Returns ``0.0`` when the numerator
        is zero or the denominator guard is triggered.

    Notes
    -----
    A small epsilon (``1e-12``) guards the denominator against division-by-zero
    when *autonomy_priv*, *equity_data*, and *phi_mersey* are all zero.
    """
    _EPSILON = 1e-12

    numerator = rinse_sum + s_sloth
    denominator = (autonomy_priv + equity_data) * phi_mersey

    if numerator == 0.0:
        return 0.0

    roi_dig = numerator / (denominator + _EPSILON)
    return max(0.0, roi_dig)


# ---------------------------------------------------------------------------
# 3.  OUSH Handshake  (Finality / Block-Lock)
# ---------------------------------------------------------------------------

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
