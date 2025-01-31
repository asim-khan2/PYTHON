import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angry Birds Clone")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Physics constants
GRAVITY = 0.5

# Game objects
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = RED
        self.dragging = False
        self.vel_x = 0
        self.vel_y = 0
        self.flying = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        if self.flying:
            self.vel_y += GRAVITY
            self.x += self.vel_x
            self.y += self.vel_y

        if self.y > HEIGHT - self.radius:  # Bounce off the ground
            self.y = HEIGHT - self.radius
            self.vel_y *= -0.7
            self.vel_x *= 0.7

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.color = GREEN
        self.hit = False

    def draw(self):
        if not self.hit:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def check_collision(self, bird):
        if (
            self.x < bird.x < self.x + self.width
            and self.y < bird.y < self.y + self.height
        ):
            self.hit = True

# Game setup
bird = Bird(150, 450)
targets = [Target(600, 500), Target(650, 450), Target(700, 500)]
running = True

# Main game loop
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not bird.flying:
            if math.hypot(bird.x - event.pos[0], bird.y - event.pos[1]) < bird.radius:
                bird.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP and bird.dragging:
            bird.dragging = False
            bird.flying = True
            bird.vel_x = (bird.x - event.pos[0]) * 0.1
            bird.vel_y = (bird.y - event.pos[1]) * 0.1

        elif event.type == pygame.MOUSEMOTION and bird.dragging:
            bird.x, bird.y = event.pos

    # Update game objects
    bird.update()
    for target in targets:
        target.check_collision(bird)

    # Draw game objects
    bird.draw()
    for target in targets:
        target.draw()

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
