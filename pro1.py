import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.ship2 = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship1.update()
            self.ship2.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship1.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship1.moving_left = True
        elif event.key == pygame.K_d:
            self.ship2.moving_right = True
        elif event.key == pygame.K_a:
            self.ship2.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship1.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship1.moving_left = False
        elif event.key == pygame.K_d:
            self.ship2.moving_right = False
        elif event.key == pygame.K_a:
            self.ship2.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship1.blitme()
        self.ship2.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
