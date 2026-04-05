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

## ENKI FLOW: The 29th Node (Real-World Sim Game)

A real-world simulation game built on the Sovereign OS engine.

```
/games
  enki_flow.py   # ENKI FLOW — pilot a Drone to harvest Kinetic Energy pulses
```

**Controls**

| Key        | Action            |
|------------|-------------------|
| `↑` Up     | Move Drone up     |
| `↓` Down   | Move Drone down   |
| Close window | Exit           |

**HUD**

- **KINETIC HARVEST** — number of golden energy pulses collected.
- **BASE FREQUENCY** — the God-Mind base frequency (10^47).

**Run the game**

```bash
pip install pygame
python games/enki_flow.py
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
