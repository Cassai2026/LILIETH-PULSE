"""
LILIETH-PULSE Game — Sprite Classes
======================================
Defines the three core sprite types used by the game:

  * Pilot      — the player-controlled sovereign agent
  * EquityNode — harvestable energy nodes (Level 1)
  * FlowGate   — Venturi acceleration gates (Level 2)
"""

from __future__ import annotations

import random

import pygame

from game.constants import (
    WIDTH,
    HEIGHT,
    CYAN,
    GREEN,
    WALL_HEIGHT,
    PILOT_BOOST,
    PILOT_SPEED_LVL1,
    NODE_SPEED,
    GATE_SPEED,
)


class Pilot(pygame.sprite.Sprite):
    """The player-controlled sovereign agent."""

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect(centerx=100, centery=HEIGHT // 2)
        self.speed = PILOT_SPEED_LVL1
        # Boost tracking
        self._boost_timer: int = 0  # frames remaining in speed boost

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Clamp inside screen
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

        # Count down any active speed boost
        if self._boost_timer > 0:
            self._boost_timer -= 1
            if self._boost_timer == 0:
                self.speed -= PILOT_BOOST

    def apply_boost(self, boost_frames: int = 120) -> None:
        """Apply a temporary speed boost for *boost_frames* frames.

        Stacks safely: only one boost timer runs at a time; if a new gate is
        hit while a boost is already active the timer resets without adding
        the bonus a second time.

        Parameters
        ----------
        boost_frames:
            Number of frames the boost lasts (~2 s at 60 FPS).
        """
        if self._boost_timer == 0:
            # No active boost — add the bonus now
            self.speed += PILOT_BOOST
        # (Re-)start the countdown regardless, refreshing an existing boost
        self._boost_timer = boost_frames


class EquityNode(pygame.sprite.Sprite):
    """Harvestable sovereign-energy node (Level 1).

    Scrolls left across the screen.  Collected by the :class:`Pilot` on contact.
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(
            x=WIDTH + 20,
            y=random.randint(20, HEIGHT - 40),
        )
        self.speed = NODE_SPEED

    def update(self) -> None:
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()


class FlowGate(pygame.sprite.Sprite):
    """Venturi Acceleration Gate (Level 2).

    A tall, narrow gate that scrolls left.  Colliding with it gives the
    :class:`Pilot` a temporary speed boost.  Spawns within the canal zone
    (between the two wall strips).
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((10, 150))
        self.image.fill((0, 255, 150))  # Neon Mint
        self.rect = self.image.get_rect(
            x=WIDTH + 20,
            y=random.randint(WALL_HEIGHT + 10, HEIGHT - WALL_HEIGHT - 160),
        )
        self.speed = GATE_SPEED

    def update(self) -> None:
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
