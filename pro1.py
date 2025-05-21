import sys
import pygame
from settings import Settings  
from ship import Ship
from ship2 import Ship2
from wall import Wall
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.gameActive = True
        self.ship = Ship(self)
        self.ship2 = Ship2(self)
        self.sb = Scoreboard(self)
        self.bg_color = self.settings.bg_color
        self.walls = []
        self.create_walls()

    def create_walls(self):
        firstplace = 208
        for i in range(6):
            wall = Wall(self, 750, firstplace)
            self.walls.append(wall)
            firstplace += 64

        firstplace = 0
        for i in range(5):
            wall = Wall(self, firstplace, 64)
            self.walls.append(wall)
            firstplace += 64

        firstplace = 64
        for i in range(4):
            wall = Wall(self, 320, firstplace)
            self.walls.append(wall)
            firstplace += 64

        firstplace =672
        for i in range(4):
            wall = Wall(self, 1116, firstplace)
            self.walls.append(wall)
            firstplace -= 64

        firstplace = 1116
        for i in range(6):
            wall = Wall(self, firstplace, 672)
            self.walls.append(wall)
            firstplace += 64


    def run_game(self):
        while True:
            self._check_events()
            if self.gameActive:
                self.ship.update(self.ship2)
                self.ship2.update(self.ship)
            self._update_screen()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.ship2.moving_up = True
        elif event.key == pygame.K_a:
            self.ship2.moving_left = True
        elif event.key == pygame.K_s:
            self.ship2.moving_down = True
        elif event.key == pygame.K_d:
            self.ship2.moving_right = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.ship2.moving_up = False
        elif event.key == pygame.K_a:
            self.ship2.moving_left = False
        elif event.key == pygame.K_s:
            self.ship2.moving_down = False
        elif event.key == pygame.K_d:
            self.ship2.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.ship2.blitme()
        self.sb.show_scores()
        for wall in self.walls:
            wall.blitme()
        


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
