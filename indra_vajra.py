import pygame
import random
import sys

WIDTH, HEIGHT = 1000, 700
FPS = 60

CYAN = (0, 255, 255)
GOLD = (255, 215, 0)
WHITE = (255, 255, 255)
DEEP_BLUE = (0, 20, 50)
VITALITY_GREEN = (50, 255, 50)


class InductionNode(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, CYAN, [(30, 0), (0, 60), (60, 60)], 3)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        self.mu_cu = 98.4

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 15
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 15


class TidalBore(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = random.randint(250, 550)
        self.image = pygame.Surface((self.width, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(
            x=random.randint(0, WIDTH - self.width), y=-50
        )
        self.speed = 18

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Indra-Vajra Kinetic Harvester")
    clock = pygame.time.Clock()
    font_hud = pygame.font.SysFont("monospace", 20, True)

    pilot = InductionNode()
    all_sprites = pygame.sprite.Group(pilot)
    bores = pygame.sprite.Group()
    equity = 0.0
    progress = 0.0
    running = True

    while running:
        screen.fill(DEEP_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if random.random() < 0.04:
            b = TidalBore()
            all_sprites.add(b)
            bores.add(b)

        all_sprites.update()

        if pygame.sprite.spritecollide(pilot, bores, True):
            equity += 1850 * (pilot.mu_cu / 100)
            progress += 0.5
            pygame.draw.rect(screen, CYAN, (0, 0, WIDTH, HEIGHT), 6)

        screen.blit(
            font_hud.render(f"KINETIC EQUITY: \xa3{equity:,.2f} / \xa3117.7M", True, GOLD),
            (20, 20),
        )
        screen.blit(
            font_hud.render(f"CONDUCTIVITY (mu_cu): {pilot.mu_cu}%", True, CYAN),
            (20, 55),
        )

        # Conductivity bar
        pygame.draw.rect(screen, (40, 40, 40), (20, 85, 200, 15))
        pygame.draw.rect(screen, CYAN, (20, 85, int(pilot.mu_cu * 2), 15))

        # Progress bar
        pygame.draw.rect(screen, (40, 40, 40), (WIDTH // 2 - 200, HEIGHT - 50, 400, 25))
        pygame.draw.rect(
            screen,
            VITALITY_GREEN,
            (WIDTH // 2 - 200, HEIGHT - 50, int((progress / 100) * 400), 25),
        )

        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
