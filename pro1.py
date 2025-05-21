import sys
import pygame
from settings import Settings  
from ship import Ship
from ship2 import Ship2
from wall import Wall

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) 
        self.ship2 = Ship2(self)
        self.bg_color = self.settings.bg_color
        self.walls = []
        self.create_walls()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            # elif event.type == pygame.KEYUP:
            #      if event.key == pygame.K_RIGHT:
            #         self.ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #         self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.bg_color) 
        self.ship.blitme()
        self.ship2.blitme()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
