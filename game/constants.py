"""
LILIETH-PULSE Game — Constants
================================
Shared constants for all game modules.
"""

# --- Display ---
WIDTH = 800
HEIGHT = 600
FPS = 60

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 220)
GREEN = (0, 200, 100)
YELLOW = (255, 220, 0)

# --- Level 2 Specific Constants ---
LEVEL_2_THRESHOLD = 50   # Transition after 50 nodes harvested
WALL_COLOR = (150, 75, 0)  # Earthy/Industrial canal walls
WALL_HEIGHT = 80           # Pixel height of each canal wall strip

# --- Pilot ---
PILOT_SPEED_LVL1 = 6
PILOT_SPEED_LVL2 = 10     # Faster baseline speed in the canal
PILOT_BOOST = 5            # Speed bonus on FlowGate hit

# --- Equity Node spawning (Level 1) ---
NODE_SPAWN_CHANCE = 0.02   # Per-frame probability
NODE_SPEED = 5

# --- Flow Gate spawning (Level 2) ---
GATE_SPAWN_CHANCE = 0.01   # Per-frame probability
GATE_SPEED = 12
