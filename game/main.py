"""
LILIETH-PULSE — Sovereign Game
================================
A two-level side-scrolling game inspired by the LILIETH Sovereign OS.

Level 1 — Equity Harvest
    Collect glowing equity nodes streaming from the right.
    Once 50 nodes have been harvested the system transitions to Level 2.

Level 2 — Manchester Terminal (The Canal)
    The playable field narrows as industrial canal walls close in from the
    top and bottom.  Venturi FlowGates scroll into view; colliding with
    one grants the pilot a 2-second speed boost.

Controls
--------
    W / ↑   — move up
    S / ↓   — move down
    A / ←   — move left
    D / →   — move right
    ESC     — quit
"""

from __future__ import annotations

import random
import sys

import pygame

from game.constants import (
    BLACK,
    CYAN,
    FPS,
    GATE_SPAWN_CHANCE,
    HEIGHT,
    LEVEL_2_THRESHOLD,
    NODE_SPAWN_CHANCE,
    PILOT_SPEED_LVL2,
    WALL_COLOR,
    WALL_HEIGHT,
    WHITE,
    WIDTH,
    YELLOW,
)
from game.sprites import EquityNode, FlowGate, Pilot


def _draw_hud(
    screen: pygame.Surface,
    font: pygame.font.Font,
    harvested: int,
    level: int,
) -> None:
    """Render the HUD overlay (score + level indicator)."""
    score_surf = font.render(f"Harvested: {harvested}", True, WHITE)
    level_surf = font.render(f"Level: {level}", True, CYAN if level == 1 else YELLOW)
    screen.blit(score_surf, (10, 10))
    screen.blit(level_surf, (10, 34))


def _draw_canal_walls(screen: pygame.Surface) -> None:
    """Draw the Level 2 industrial canal walls."""
    pygame.draw.rect(screen, WALL_COLOR, (0, 0, WIDTH, WALL_HEIGHT))
    pygame.draw.rect(screen, WALL_COLOR, (0, HEIGHT - WALL_HEIGHT, WIDTH, WALL_HEIGHT))


def main() -> None:
    """Entry point — run the LILIETH-PULSE game."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LILIETH-PULSE — Sovereign Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    # --- Sprite groups ---
    all_sprites: pygame.sprite.Group = pygame.sprite.Group()
    nodes: pygame.sprite.Group = pygame.sprite.Group()
    gates: pygame.sprite.Group = pygame.sprite.Group()

    # --- Player ---
    pilot = Pilot()
    all_sprites.add(pilot)

    # --- State ---
    harvested_equity: int = 0
    level: int = 1
    running: bool = True

    while running:
        clock.tick(FPS)

        # ------------------------------------------------------------------ #
        # Event handling                                                       #
        # ------------------------------------------------------------------ #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # ------------------------------------------------------------------ #
        # Level 1 → Level 2 transition                                        #
        # ------------------------------------------------------------------ #
        if harvested_equity >= LEVEL_2_THRESHOLD and level == 1:
            level = 2
            pilot.speed = PILOT_SPEED_LVL2  # Faster baseline speed in the canal
            print("TRANSITION: ENTERING THE MANCHESTER TERMINAL")

        # ------------------------------------------------------------------ #
        # Spawning                                                             #
        # ------------------------------------------------------------------ #
        if level == 1:
            # Spawn equity nodes to harvest
            if random.random() < NODE_SPAWN_CHANCE:
                node = EquityNode()
                all_sprites.add(node)
                nodes.add(node)
        else:
            # Level 2: Spawn Flow Gates
            if random.random() < GATE_SPAWN_CHANCE:
                gate = FlowGate()
                all_sprites.add(gate)
                gates.add(gate)

        # ------------------------------------------------------------------ #
        # Update sprites                                                       #
        # ------------------------------------------------------------------ #
        all_sprites.update()

        # ------------------------------------------------------------------ #
        # Collision — Level 1: collect equity nodes                           #
        # ------------------------------------------------------------------ #
        node_hits = pygame.sprite.spritecollide(pilot, nodes, True)
        harvested_equity += len(node_hits)

        # ------------------------------------------------------------------ #
        # Collision — Level 2: FlowGate boost                                 #
        # ------------------------------------------------------------------ #
        gate_hits = pygame.sprite.spritecollide(pilot, gates, True)
        if gate_hits:
            # Temporary ~2-second speed boost (120 frames at 60 FPS)
            pilot.apply_boost(boost_frames=120)

        # ------------------------------------------------------------------ #
        # Clamp pilot inside the canal walls in Level 2                       #
        # ------------------------------------------------------------------ #
        if level == 2:
            pilot.rect.top = max(pilot.rect.top, WALL_HEIGHT)
            pilot.rect.bottom = min(pilot.rect.bottom, HEIGHT - WALL_HEIGHT)

        # ------------------------------------------------------------------ #
        # Drawing                                                              #
        # ------------------------------------------------------------------ #
        screen.fill(BLACK)

        if level == 2:
            _draw_canal_walls(screen)

        all_sprites.draw(screen)
        _draw_hud(screen, font, harvested_equity, level)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
