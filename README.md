# LILIETH-PULSE — Sovereign OS Kernel

A Python **Foundry** that interprets four custom LILIETH file types, gates
ethical commands through the S.U.E. balance engine, harvests kinetic energy
from road traffic, and secures every privileged operation behind a biometric
root lock.

---

## Repository Structure

```
/core
  algorithms.py      # S.U.E. Validator · Indra-Vajra Harvester · OUSH Handshake · Φ_fire · ROI_env
  interpreter.py     # Extensible LiliethParser for .v / .kg / .4d / .ai files
  compiler.py        # Compiles AST nodes → sealed Bytecode via OUSH finality

/biometrics
  root_auth.py       # Cyan-on-Black two-factor root authentication

/protocols
  init_mesh.v        # Vajra — Quad-Vector mesh initialisation
  stretford_audit.4d # Eternius — A56 kinetic-slab spatial audit
  lilieth_core.ai    # Animus — 14+1 Sovereign Pillars governance
  phlogiston.kg      # KONG — Vulcan Kiln plasma gasification (Section IV)

/data
  memory_map.json    # Saline Lattice — runtime state of the Sovereign Mesh

/tests
  test_lilieth.py    # 51 pytest tests covering all modules
```

---

## Custom File Types

| Extension | Name      | Purpose                                    |
|-----------|-----------|--------------------------------------------|
| `.v`      | Vajra     | Logic / Induction math commands            |
| `.kg`     | KONG      | Physical execution / Material integrity    |
| `.4d`     | Eternius  | Spatial / Temporal blueprints              |
| `.ai`     | Animus    | Ethical governance / 14+1 Pillars          |

**Token syntax:** `<action-letters><scale-digits> [args…]`
e.g. `give10001 community_resource` or `take500 sky_ionic_bleed`

---

## Core Algorithms

### 1 · S.U.E. (Sovereign Unified Equation) Validator

```python
from core.algorithms import calculate_sue_score

virtues = {'love': 0.9, 'truth': 0.85, 'courage': 0.8,
           'wisdom': 0.88, 'justice': 0.82, 'temperance': 0.75, 'sovereignty': 0.95}
sins    = {'greed': 0.1, 'sloth': 0.05, 'wrath': 0.08,
           'envy': 0.06, 'pride': 0.07, 'gluttony': 0.04, 'lust': 0.03}

score = calculate_sue_score(virtues, sins)
# score > 1.0 → action permitted (Pulse confirmed)
# score ≤ 1.0 → action blocked  (Static Sloth)
```

All `give` commands in `.ai` files are automatically gated through this validator.

### 2 · Indra-Vajra Kinetic Harvester

```python
from core.algorithms import harvest_kinetic_energy

joules = harvest_kinetic_energy(traffic_density=100.0, velocity_avg=30.0)
# → 2939.98 Sovereign Joules
```

The KONG interpreter listens for `take` commands in `.v` files and triggers
this harvester automatically via a registered hook.

### 3 · OUSH Finality Handshake

```python
from core.algorithms import oush_handshake

oush_handshake("NODE_42", "ARCHITECT_ALPHA")
# NODE 42: SOVEREIGNTY LOCKED. OUSH.
```

Every compiled bytecode block is sealed with an OUSH handshake before dispatch.

### 4 · Φ_fire (Phlogiston Thermal Induction)

```python
from core.algorithms import calculate_phi_fire

phi = calculate_phi_fire(
    m_waste=47000.0,   # kg input from 47,000 residents
    delta_tox=0.01,    # toxicity coefficient (approaches 0 for plasma)
    q_plasma=5.0,      # MJ/kg plasma heat flux
    delta_t=4800.0,    # K thermal differential (Vulcan Kiln → Sovereign Spine)
    e_ash_sum=2350.0,  # kg mineral equity of Bio-Active Ash (E_ash)
)
# Φ_fire = (M_waste × δ_tox) / ((Q_plasma × ΔT) + Σ_E_ash)
```

Higher Φ_fire indicates greater toxic-mass conversion per unit of thermal-mineral output.
Triggered automatically by `dissociate` commands in `.kg` protocol files.

### 5 · ROI_env (Environmental Return on Investment)

```python
from core.algorithms import calculate_roi_env

roi = calculate_roi_env(
    carbon_seq=1200.0,      # tonnes C locked in 100 Ash Trees + vitrified slag
    soil_vit=850.0,         # soil vitality index from E_ash application
    growth_multiplier=5.0,  # Λ — Sovereign Forest accelerated biological rate
    landfill_vol=94000.0,   # m³ static waste removed from Stretford Meadows
    emission_stat=3100.0,   # tCO₂e baseline displaced by Vulcan Kiln
)
# ROI_env = ((Carbon_seq + Soil_vit) × Λ) / (Landfill_vol + Emission_stat)
# roi > 1.0 → net environmental gain (regeneration outweighs historical damage)
```

Triggered automatically by `sequester` commands in `.kg` protocol files.

---

## Quick Start

```python
from core.interpreter import LiliethParser

parser = LiliethParser()

# Parse & execute the Animus governance protocol
results = parser.parse_and_execute("protocols/lilieth_core.ai")
for r in results:
    print(r.get("animus_status"), r.get("sue_score"))
```

```python
from core.compiler import LiliethCompiler

compiler = LiliethCompiler()
bytecode = compiler.compile_file("protocols/init_mesh.v", node_id="mesh_node_1")
print(bytecode.to_dict())
```

```python
from biometrics.root_auth import RootSession

with RootSession("ARCHITECT_ALPHA", "LILIETH_BIO_ROOT_v1", node_id="admin") as s:
    print("Root access granted — Sovereign OS initialising…")
```

---

## Running Tests

```bash
pip install pytest
pytest tests/test_lilieth.py -v
```

---

## Extending the Parser

Register any new interpreter at runtime:

```python
from core.interpreter import BaseInterpreter, LiliethParser

class MyInterpreter(BaseInterpreter):
    extension = ".my"
    def execute_node(self, node):
        return {"custom_result": node.action}

parser = LiliethParser()
parser.register_interpreter(MyInterpreter())
nodes = parser.parse_source("do100 payload\n", ".my")
print(parser.execute(nodes))
```
