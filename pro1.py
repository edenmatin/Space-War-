import sys
import pygame
from settings import Settings  
from ship import Ship
from ship2 import Ship2
from wall import Wall
from scoreboard import Scoreboard
from bullet import Bullet  

class AlienInvasion:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("./music/gamemusic.mp3")  
        pygame.mixer.music.play(start=50)                
        pygame.mixer.music.set_volume(1.0)         

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = self.settings.bg_color
        self.sb = Scoreboard(self)
        self.reset_match()

        self.gameActive = True
        self.win_time = None
        self.pause_duration = 2000  
        self.last_winner = None  

        self.walls = []
        self.create_walls()

    def create_walls(self):
        self.walls = []
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

        firstplace = 672
        for i in range(4):
            wall = Wall(self, 1116, firstplace)
            self.walls.append(wall)
            firstplace -= 64

        firstplace = 1116
        for i in range(6):
            wall = Wall(self, firstplace, 672)
            self.walls.append(wall)
            firstplace += 64

    def reset_match(self):
        self.ship = Ship(self)
        self.ship2 = Ship2(self)
        self.bullets1 = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            current_time = pygame.time.get_ticks()

            if self.gameActive:
                self.ship.update(self.ship2)
                self.ship2.update(self.ship)
                self.bullets1.update()
                self.bullets2.update()

                for bullet in self.bullets1:
                    if bullet.rect.colliderect(self.ship.rect):
                        bullet.kill()
                        self.sb.increase_score1(1)
                        self.last_winner = "player1"
                        self.gameActive = False
                        self.win_time = current_time

                for bullet in self.bullets2:
                    if bullet.rect.colliderect(self.ship2.rect):
                        bullet.kill()
                        self.sb.increase_score2(1)
                        self.last_winner = "player2"
                        self.gameActive = False
                        self.win_time = current_time

                for bullet in self.bullets1:
                    if pygame.sprite.spritecollideany(bullet, self.walls):
                        bullet.kill()
                for bullet in self.bullets2:
                    if pygame.sprite.spritecollideany(bullet, self.walls):
                        bullet.kill()

            elif self.win_time and current_time - self.win_time > self.pause_duration:
                self.reset_match()
                self.gameActive = True
                self.win_time = None
                self.last_winner = None

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
        elif event.key == pygame.K_SPACE:
            if len(self.bullets1) < 3:
                bullet = Bullet(self, self.ship2, direction="right")  
                self.bullets1.add(bullet)
        elif event.key == pygame.K_KP_ENTER:
            if len(self.bullets2) < 3:
                bullet = Bullet(self, self.ship, direction="left")  
                self.bullets2.add(bullet)

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

        for bullet in self.bullets1:
            bullet.draw_bullet()
        for bullet in self.bullets2:
            bullet.draw_bullet()

        self.sb.show_scores()
        for wall in self.walls:
            wall.blitme()

        if not self.gameActive and self.win_time:
            font = pygame.font.SysFont(None, 72)
            if self.last_winner == "player1":
                msg="Player 1 Wins!"
                color = (0, 180, 255)
            elif self.last_winner == "player2":
                msg="Player 2 Wins!"
                color = (0, 0, 0)
            else:
                msg = ""
                color = (0, 0, 0)

            if msg:
                win_image = font.render(msg, True, color)
                win_rect = win_image.get_rect(center=self.screen.get_rect().center)
                self.screen.blit(win_image, win_rect)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
