import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game, ship, direction):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.direction = direction

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        if direction == "right":
            self.rect.midleft = ship.rect.midright
        else:  # direction == "left"
            self.rect.midright = ship.rect.midleft

        self.x = float(self.rect.x)

    def update(self):
        if self.direction == "right":
            self.x += self.settings.bullet_speed
        else:
            self.x -= self.settings.bullet_speed

        self.rect.x = self.x

        if self.rect.right < 0 or self.rect.left > self.screen.get_width():
            self.kill()

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

