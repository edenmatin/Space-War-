import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self, ai_game, x, y):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/wall1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def create_walls(self):

        z = 200
        for i in range(8):
            wall = Wall(self, 750, z)
            self.walls.append(wall)
            z += 64
        z = 0
        for i in range(4):
            wall = Wall(self, z, 100)
            self.walls.append(wall)
            z += 64
        z = 100
        for i in range(3):
            wall = Wall(self, 300, z)
            self.walls.append(wall)
            z += 64
       