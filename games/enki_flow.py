import pygame
import random
import sys

# --- Sovereign Constants & OS Settings ---
WIDTH, HEIGHT = 1000, 700
FPS = 60
CYAN = (0, 255, 255)
GOLD = (255, 215, 0)
DEEP_BLUE = (0, 20, 50)
SLOTH_GREY = (60, 60, 60)
VITALITY_GREEN = (50, 255, 50)

# --- Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ENKI FLOW: THE RECLAMATION")
clock = pygame.time.Clock()
font_main = pygame.font.SysFont("monospace", 22, bold=True)
font_hud = pygame.font.SysFont("monospace", 18)

# --- Game Entities ---

class SovereignPilot(pygame.sprite.Sprite):
    """The Pilot of the Etheric Mash (Paul Edward Cassidy)"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(CYAN)
        # Adding a 'shield' effect for the Athletic Buffer
        pygame.draw.rect(self.image, VITALITY_GREEN, (0, 0, 50, 30), 2)
        self.rect = self.image.get_rect(center=(100, HEIGHT // 2))
        self.speed = 8
        self.vitality = 100

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 50:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT - 50:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 20:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH // 2:
            self.rect.x += self.speed

class KineticNode(pygame.sprite.Sprite):
    """Harvestable H4O / Tidal Energy"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(x=WIDTH + 20, y=random.randint(100, HEIGHT - 100))
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

class StaticSloth(pygame.sprite.Sprite):
    """Council Debt / Friction Obstacles"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(SLOTH_GREY)
        pygame.draw.line(self.image, (255, 0, 0), (0, 0), (40, 40), 3)
        self.rect = self.image.get_rect(x=WIDTH + 20, y=random.randint(100, HEIGHT - 100))
        self.speed = 6

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

# --- Main Game Engine ---

def main():
    pilot = SovereignPilot()
    all_sprites = pygame.sprite.Group(pilot)
    nodes = pygame.sprite.Group()
    sloths = pygame.sprite.Group()

    harvested_equity = 0
    base_frequency = 47  # 10^47 logic
    running = True
    game_state = "RUNNING"

    while running:
        screen.fill(DEEP_BLUE)

        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == "RUNNING":
            keys = pygame.key.get_pressed()
            pilot.update(keys)

            # 2. Spawning Logic
            if random.random() < 0.04:
                node = KineticNode()
                all_sprites.add(node)
                nodes.add(node)

            if random.random() < 0.02:
                sloth = StaticSloth()
                all_sprites.add(sloth)
                sloths.add(sloth)

            # 3. Collision Logic
            # Harvesting Energy
            harvest_hits = pygame.sprite.spritecollide(pilot, nodes, True)
            for hit in harvest_hits:
                harvested_equity += 1

            # Hitting Sloth (Losing Vitality)
            damage_hits = pygame.sprite.spritecollide(pilot, sloths, True)
            for hit in damage_hits:
                pilot.vitality -= 10
                if pilot.vitality <= 0:
                    game_state = "DEBT_TRAP"

            # 4. Movement
            nodes.update()
            sloths.update()

            # 5. Drawing HUD
            # Draw the Mersey Flow lines
            for i in range(0, HEIGHT, 100):
                pygame.draw.line(screen, (0, 50, 100), (0, i), (WIDTH, i), 2)

            equity_text = font_main.render(f"SOVEREIGN EQUITY: {harvested_equity} / 47,000", True, GOLD)
            freq_text = font_hud.render(f"FREQUENCY: 10^{base_frequency} Hz", True, CYAN)
            vital_text = font_hud.render(f"ATHLETIC BUFFER (VITALITY): {pilot.vitality}%", True, VITALITY_GREEN)

            screen.blit(equity_text, (20, 20))
            screen.blit(freq_text, (20, 55))
            screen.blit(vital_text, (WIDTH - 400, 20))

            all_sprites.draw(screen)

        elif game_state == "DEBT_TRAP":
            over_text = font_main.render("STATIC SLOTH DETECTED - REBOOTING ENKI FLOW", True, (255, 0, 0))
            screen.blit(over_text, (WIDTH // 2 - 300, HEIGHT // 2))
            # Logic to reset could go here

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
