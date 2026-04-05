import pygame
import random

# --- Sovereign Constants ---
WIDTH, HEIGHT = 800, 600
FPS = 60
BLUE_MERSEY = (0, 70, 140)
CYAN_NODE = (0, 255, 255)
STATIC_SLOTH = (100, 100, 100)
TEXT_COLOR = (255, 255, 255)


class Drone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(CYAN_NODE)
        self.rect = self.image.get_rect(center=(100, HEIGHT // 2))
        self.speed = 7

    def update(self, keys=None):
        if keys is None:
            return
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed


class KineticEnergy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 215, 0))  # Golden Kinetic Pulse
        self.rect = self.image.get_rect(x=WIDTH, y=random.randint(50, HEIGHT - 50))
        self.speed = random.randint(4, 8)

    def update(self, keys=None):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()


# --- Main Engine ---
def run_synthesis():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ENKI FLOW: The 29th Node")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 20)

    drone = Drone()
    all_sprites = pygame.sprite.Group(drone)
    energies = pygame.sprite.Group()

    score = 0
    running = True

    while running:
        screen.fill(BLUE_MERSEY)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Spawn Kinetic Pulses
        if random.random() < 0.05:
            new_energy = KineticEnergy()
            all_sprites.add(new_energy)
            energies.add(new_energy)

        # Update — pass keys so the Drone responds to input
        all_sprites.update(keys)

        # Collisions (Harvesting)
        hits = pygame.sprite.spritecollide(drone, energies, True)
        for hit in hits:
            score += 1

        # Draw
        all_sprites.draw(screen)

        # HUD: Sovereign Stats
        score_txt = font.render(f"KINETIC HARVEST: {score}", True, TEXT_COLOR)
        freq_txt = font.render("BASE FREQUENCY: 10^47", True, CYAN_NODE)
        screen.blit(score_txt, (20, 20))
        screen.blit(freq_txt, (20, 50))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run_synthesis()
