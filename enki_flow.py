"""
ENKI FLOW: THE 2046 HORIZON
============================
A Sovereign action game set in 2046.
Pilot ENKI through a gauntlet of Council Auditors
and reclaim the £117.7 M success fee at Padstow Anchor.

Controls
--------
Arrow keys — move
SPACE      — fire
ESC        — quit / return to menu
"""

import pygame
import random
import sys

# --- Sovereign Constants ---
WIDTH, HEIGHT = 1000, 700
FPS = 60
CYAN = (0, 255, 255)
GOLD = (255, 215, 0)
DEEP_BLUE = (0, 20, 50)
SLOTH_GREY = (60, 60, 60)
VITALITY_GREEN = (50, 255, 50)
BOSS_RED = (200, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ENKI FLOW: THE 2046 HORIZON")
clock = pygame.time.Clock()
font_main = pygame.font.SysFont("monospace", 30, bold=True)
font_hud = pygame.font.SysFont("monospace", 18)

# --- Entities ---

class SovereignPilot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        self.image.fill(CYAN)
        pygame.draw.rect(self.image, VITALITY_GREEN, (0, 0, 50, 30), 2)
        self.rect = self.image.get_rect(center=(100, HEIGHT // 2))
        self.speed = 8
        self.vitality = 100
        self._shoot_cooldown = 0

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 80:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT - 80:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 20:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 50:
            self.rect.x += self.speed
        if self._shoot_cooldown > 0:
            self._shoot_cooldown -= 1

    def shoot(self):
        """Return a new Projectile if cooldown allows, else None."""
        if self._shoot_cooldown == 0:
            self._shoot_cooldown = 12
            return Projectile(self.rect.right, self.rect.centery,
                              speed=14, color=CYAN, direction=1)
        return None


class AuditorBoss(pygame.sprite.Sprite):
    """The 'Silly Boy' Council Auditor."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((120, 120))
        self.image.fill(SLOTH_GREY)
        pygame.draw.rect(self.image, BOSS_RED, (0, 0, 120, 120), 5)
        self.rect = self.image.get_rect(center=(WIDTH + 150, HEIGHT // 2))
        self.health = 100
        self.direction = 1
        self._shoot_timer = 0
        self._shoot_interval = 80   # frames between boss shots

    def update(self):
        # Slide onto screen, then oscillate vertically
        if self.rect.x > WIDTH - 200:
            self.rect.x -= 2
        else:
            self.rect.y += 5 * self.direction
            if self.rect.top < 100 or self.rect.bottom > HEIGHT - 100:
                self.direction *= -1

        if self._shoot_timer > 0:
            self._shoot_timer -= 1

    def shoot(self):
        """Return a new EnemyShot if cooldown allows, else None."""
        if self.rect.x <= WIDTH - 200 and self._shoot_timer == 0:
            self._shoot_timer = self._shoot_interval
            return EnemyShot(self.rect.left, self.rect.centery)
        return None

    def take_hit(self, damage: int = 10):
        self.health = max(0, self.health - damage)

    def draw_health_bar(self, surface: pygame.Surface):
        bar_x, bar_y = WIDTH - 220, 20
        bar_w, bar_h = 200, 18
        fill = int(bar_w * self.health / 100)
        pygame.draw.rect(surface, BOSS_RED, (bar_x, bar_y, bar_w, bar_h))
        pygame.draw.rect(surface, VITALITY_GREEN, (bar_x, bar_y, fill, bar_h))
        pygame.draw.rect(surface, WHITE, (bar_x, bar_y, bar_w, bar_h), 2)
        label = font_hud.render("AUDITOR HP", True, WHITE)
        surface.blit(label, (bar_x, bar_y + bar_h + 2))


class Projectile(pygame.sprite.Sprite):
    """A shot fired by the Sovereign Pilot."""

    def __init__(self, x: int, y: int, speed: int = 14,
                 color=CYAN, direction: int = 1):
        super().__init__()
        self.image = pygame.Surface((16, 6))
        self.image.fill(color)
        self.rect = self.image.get_rect(midleft=(x, y))
        self._speed = speed * direction

    def update(self):
        self.rect.x += self._speed
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.kill()


class EnemyShot(pygame.sprite.Sprite):
    """A shot fired by the AuditorBoss."""

    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.Surface((14, 8))
        self.image.fill(BOSS_RED)
        self.rect = self.image.get_rect(midright=(x, y))
        self._speed = -7

    def update(self):
        self.rect.x += self._speed
        if self.rect.right < 0:
            self.kill()


class StarField:
    """Simple parallax star background."""

    def __init__(self, count: int = 120):
        self._stars = [
            [random.randint(0, WIDTH),
             random.randint(0, HEIGHT),
             random.uniform(0.5, 2.5)]
            for _ in range(count)
        ]

    def update_and_draw(self, surface: pygame.Surface):
        for star in self._stars:
            star[0] -= star[2]
            if star[0] < 0:
                star[0] = WIDTH
                star[1] = random.randint(0, HEIGHT)
            radius = max(1, int(star[2]))
            brightness = min(255, int(star[2] * 100))
            pygame.draw.circle(surface, (brightness, brightness, brightness),
                               (int(star[0]), int(star[1])), radius)


# --- Logic Modules ---

def draw_hud(surface: pygame.Surface, pilot: SovereignPilot, score: int):
    """Render the pilot vitality bar and score."""
    # Vitality bar
    bar_x, bar_y = 20, 20
    bar_w, bar_h = 180, 18
    fill = int(bar_w * pilot.vitality / 100)
    pygame.draw.rect(surface, BOSS_RED, (bar_x, bar_y, bar_w, bar_h))
    pygame.draw.rect(surface, VITALITY_GREEN, (bar_x, bar_y, fill, bar_h))
    pygame.draw.rect(surface, WHITE, (bar_x, bar_y, bar_w, bar_h), 2)
    label = font_hud.render("VITALITY", True, WHITE)
    surface.blit(label, (bar_x, bar_y + bar_h + 2))
    # Score
    score_surf = font_hud.render(f"SCORE: {score:06d}", True, GOLD)
    surface.blit(score_surf, (20, 50))


def show_title_screen(surface: pygame.Surface) -> bool:
    """Display the title screen. Returns True to start, False to quit."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False

        surface.fill(DEEP_BLUE)
        title = font_main.render("ENKI FLOW: THE 2046 HORIZON", True, CYAN)
        sub = font_hud.render("Defeat the Council Auditor. Reclaim the Pulse.", True, GOLD)
        start = font_hud.render("Press ENTER to begin  |  ESC to quit", True, WHITE)
        surface.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))
        surface.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        surface.blit(start, start.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))
        pygame.display.flip()
        clock.tick(FPS)


def show_final_screen(surface: pygame.Surface, equity: int):
    """Victory screen shown when the Auditor Boss is defeated."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        surface.fill(DEEP_BLUE)
        title = font_main.render("THE 2046 HORIZON REACHED", True, CYAN)
        sub = font_hud.render("SUCCESS FEE RECLAIMED: £117.7M", True, GOLD)
        coords = font_hud.render("LOCATION: PADSTOW ANCHOR — ENKI SOVEREIGN NODE", True, WHITE)
        score_line = font_hud.render(f"FINAL SCORE: {equity:06d}", True, VITALITY_GREEN)
        prompt = font_hud.render("Press any key to exit", True, SLOTH_GREY)

        surface.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 90)))
        surface.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        surface.blit(coords, coords.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        surface.blit(score_line, score_line.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 55)))
        surface.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 110)))
        pygame.display.flip()
        clock.tick(FPS)


def show_game_over(surface: pygame.Surface):
    """Game-over screen."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        surface.fill(DEEP_BLUE)
        title = font_main.render("VITALITY DEPLETED — STATIC SLOTH", True, BOSS_RED)
        sub = font_hud.render("The Auditor prevails. For now.", True, WHITE)
        prompt = font_hud.render("Press any key to return", True, SLOTH_GREY)
        surface.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        surface.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        surface.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))
        pygame.display.flip()
        clock.tick(FPS)


# --- Main Game Loop ---

def run_game():
    stars = StarField()

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()
    enemy_shots = pygame.sprite.Group()

    pilot = SovereignPilot()
    boss = AuditorBoss()
    all_sprites.add(pilot, boss)

    score = 0
    running = True

    while running:
        clock.tick(FPS)

        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_SPACE:
                    shot = pilot.shoot()
                    if shot:
                        all_sprites.add(shot)
                        player_shots.add(shot)

        # --- Update ---
        keys = pygame.key.get_pressed()
        pilot.update(keys)
        boss.update()

        # Boss fires
        b_shot = boss.shoot()
        if b_shot:
            all_sprites.add(b_shot)
            enemy_shots.add(b_shot)

        for shot in list(player_shots):
            shot.update()
        for shot in list(enemy_shots):
            shot.update()

        # Player shots → boss
        hits = pygame.sprite.spritecollide(boss, player_shots, True)
        for _ in hits:
            boss.take_hit(10)
            score += 100

        # Enemy shots → pilot
        player_hits = pygame.sprite.spritecollide(pilot, enemy_shots, True)
        for _ in player_hits:
            pilot.vitality = max(0, pilot.vitality - 15)

        # Win / lose checks
        if boss.health <= 0:
            show_final_screen(screen, score)
            return
        if pilot.vitality <= 0:
            show_game_over(screen)
            return

        # --- Draw ---
        screen.fill(DEEP_BLUE)
        stars.update_and_draw(screen)

        # Separator lines
        pygame.draw.line(screen, CYAN, (0, 75), (WIDTH, 75), 1)
        pygame.draw.line(screen, CYAN, (0, HEIGHT - 75), (WIDTH, HEIGHT - 75), 1)

        all_sprites.draw(screen)

        draw_hud(screen, pilot, score)
        boss.draw_health_bar(screen)

        pygame.display.flip()


# --- Entry Point ---

def main():
    while True:
        proceed = show_title_screen(screen)
        if not proceed:
            break
        run_game()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
