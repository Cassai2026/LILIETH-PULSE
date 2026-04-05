"""
LILIETH Kernel — Core Algorithms
=================================
Three foundational algorithms that power the Sovereign OS:

  1. S.U.E. (Sovereign Unified Equation) Validator — ethical gate for .ai commands
  2. Indra-Vajra Kinetic Harvester           — converts physical motion to Sovereign Joules
  3. OUSH Handshake                          — P2P finality / block-lock signature check
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

# ---------------------------------------------------------------------------
# 4.  Biogas Induction Constant  (Section V — Φgas)
# ---------------------------------------------------------------------------

def calculate_biogas_induction(
    sources: list,
    delta_leak: float = 0.0,
) -> float:
    """Calculate the Biogas Induction Constant (Φgas) for the GasWorX mesh.

    Formula
    -------
    ``Φgas = Σ(Vsource × CCH4 × μext) − δleak``

    where each entry in *sources* contributes one term of the summation.

    Parameters
    ----------
    sources:
        A list of dicts, each containing:

        * ``v_source``  — Volume of the decomposition layer (m³).
        * ``c_ch4``     — Methane concentration as a fraction in [0.0, 1.0].
          Pockets with concentration exceeding 60 % (≥ 0.60) are considered
          high-purity and fully included; lower-purity pockets are included
          as-is (the caller may pre-filter if desired).
        * ``mu_ext``    — Extraction efficiency of the vacuum-induction copper
          straws + zeolite filters, as a fraction in [0.0, 1.0].

    delta_leak:
        Total leakage loss across the mesh (m³-equivalent).  In the
        Sovereign system this is driven toward 0; in legacy grids it can
        reach 100 % of the raw harvest.  Must be ≥ 0.

    Returns
    -------
    float
        Φgas — net harvestable biogas volume (m³-equivalent).  Clamped to 0
        so that a large leakage term can never produce a negative result.

    Raises
    ------
    ValueError
        If any source entry is missing a required key, or if a numeric value
        falls outside its valid range.
    """
    if delta_leak < 0:
        raise ValueError("delta_leak must be >= 0")

    phi_gas = 0.0
    for i, src in enumerate(sources):
        for key in ("v_source", "c_ch4", "mu_ext"):
            if key not in src:
                raise ValueError(f"Source entry {i} is missing required key {key!r}")

        v_source = float(src["v_source"])
        c_ch4 = float(src["c_ch4"])
        mu_ext = float(src["mu_ext"])

        if not (0.0 <= c_ch4 <= 1.0):
            raise ValueError(
                f"Source entry {i}: c_ch4 must be in [0.0, 1.0], got {c_ch4}"
            )
        if not (0.0 <= mu_ext <= 1.0):
            raise ValueError(
                f"Source entry {i}: mu_ext must be in [0.0, 1.0], got {mu_ext}"
            )

        phi_gas += v_source * c_ch4 * mu_ext

    return max(0.0, phi_gas - delta_leak)


# ---------------------------------------------------------------------------
# 5.  Generational ROI  (Section V — ROIgen)
# ---------------------------------------------------------------------------

def calculate_generational_roi(
    debt_inheritance: float,
    s_sloth: float,
    kernel_sync: float,
    family_sec: float,
    t_100: float = 100.0,
) -> float:
    """Calculate the Generational ROI (ROIgen) — the 100-year Sovereign return.

    Formula
    -------
    ``ROIgen = (Debt_inheritance + S_sloth) / ((Kernel_sync + Family_sec) × T100)``

    This equation measures how much "Static" burden (inherited debt, legacy
    energy costs, sloth tax) is erased per unit of Sovereign productivity
    (64-core induction × family-security shield) compounded over the 100-year
    horizon.  A value **> 1.0** confirms that the Sovereign infrastructure
    delivers more autonomy than the legacy world extracts.

    Parameters
    ----------
    debt_inheritance:
        The cumulative "Static" tax and energy-bill liability passed to the
        next generation (£ or equivalent unit).  Must be ≥ 0.
    s_sloth:
        The economic cost of legacy "Static" sloth — idle infrastructure,
        wasted energy, uncaptured biogas.  Must be ≥ 0.
    kernel_sync:
        The aggregate 64-core InductionWorX achievement level of the gifted
        masters (Harry, Jack, Marie) — a dimensionless index > 0.
    family_sec:
        The CareWorX family-security coefficient: composite score of on-site
        health, psychological support, and daycare provision.  Must be > 0.
    t_100:
        The Sovereign horizon in years (default 100).  Must be > 0.

    Returns
    -------
    float
        ROIgen index.  A result **> 1.0** means the Sovereign Spine delivers
        a net-positive generational return; ≤ 1.0 indicates the legacy burden
        still outweighs Sovereign productivity.

    Raises
    ------
    ValueError
        If any parameter violates its domain constraint (e.g. negative debt,
        zero or negative denominator terms).
    """
    if debt_inheritance < 0:
        raise ValueError("debt_inheritance must be >= 0")
    if s_sloth < 0:
        raise ValueError("s_sloth must be >= 0")
    if kernel_sync <= 0:
        raise ValueError("kernel_sync must be > 0")
    if family_sec <= 0:
        raise ValueError("family_sec must be > 0")
    if t_100 <= 0:
        raise ValueError("t_100 must be > 0")

    numerator = debt_inheritance + s_sloth
    denominator = (kernel_sync + family_sec) * t_100
    return numerator / denominator


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
