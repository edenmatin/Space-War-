import pygame

class Ship2:
    def __init__(self, ai_game):
        self.ai_game = ai_game  
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("./images/rocket2.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, other_ship):
        new_rect = self.rect.copy()
        if self.moving_right and self.rect.right < self.screen_rect.right:
            new_rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            new_rect.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            new_rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            new_rect.y += self.settings.ship_speed
        scoreboard1_rect = pygame.Rect(-40, 0, 150, 60)
        scoreboard2_rect = pygame.Rect(1380, 0, 150, 60)
        if new_rect.colliderect(scoreboard1_rect) or new_rect.colliderect(scoreboard2_rect):
            return
        for wall in self.ai_game.walls:
            if new_rect.colliderect(wall.rect):
                return
        if new_rect.colliderect(other_ship.rect):
            return

        self.rect = new_rect
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

