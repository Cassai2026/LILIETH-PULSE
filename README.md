# LILIETH-PULSE — Sovereign OS Kernel

A Python **Foundry** that interprets four custom LILIETH file types, gates
ethical commands through the S.U.E. balance engine, harvests kinetic energy
from road traffic, and secures every privileged operation behind a biometric
root lock.

---

## Repository Structure

```
/core
  algorithms.py      # S.U.E. Validator · Indra-Vajra Harvester · OUSH Handshake
  interpreter.py     # Extensible LiliethParser for .v / .kg / .4d / .ai files
  compiler.py        # Compiles AST nodes → sealed Bytecode via OUSH finality

/biometrics
  root_auth.py       # Cyan-on-Black two-factor root authentication

/protocols
  init_mesh.v        # Vajra — Quad-Vector mesh initialisation
  stretford_audit.4d # Eternius — A56 kinetic-slab spatial audit
  lilieth_core.ai    # Animus — 14+1 Sovereign Pillars governance
  aetheric_mesh.v    # Vajra — Section VI Aetheric Mesh & Abzu Vault initialisation

/data
  memory_map.json    # Saline Lattice — runtime state of the Sovereign Mesh

/tests
  test_lilieth.py    # 34 pytest tests covering all modules
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

### 4 · Aetheric Induction Constant (Ψ_sync) — Section VI

```python
from core.algorithms import calculate_aetheric_sync

psi = calculate_aetheric_sync(
    b_width=1000.0,      # Aetheric Bandwidth (Dual-Tetrahedron capacity)
    kappa_ether=0.85,    # Dielectric Permittivity (ionisation-based)
    beth_kernel=1.0,     # Kernel Integrity (1.0 = zero Static bloat)
    delta_lag=5.0,       # Decision Latency (nanoseconds)
    sigma_noise=0.02,    # Residual noise coefficient
)
# psi ≈ 1.176e-4  (Sovereign sync index)
```

### 5 · Digital ROI Equation (ROI_dig) — Section VI

```python
from core.algorithms import calculate_digital_roi

roi = calculate_digital_roi(
    autonomy_priv=1e6,   # Value of sovereign, un-throttled communication
    equity_data=1e28,    # Abzu collective knowledge equity (£10 Octillion)
    rinse_sum=5e5,       # Friction eliminated (fees, data-theft, ads)
    s_sloth=0.05,        # Static Sloth coefficient from S.U.E. register
    phi_mersey=1.618,    # Mersey Sovereign Multiplier
)
# roi → value approaching 0 means Cognitive Freedom far exceeds legacy friction
```

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
