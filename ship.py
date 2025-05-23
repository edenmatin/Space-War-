import pygame

class Ship:
    def __init__(self, ai_game):
        self.ai_game = ai_game 
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("./images/rocket (1).png")
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright

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

        min_x = 0
        max_x = self.screen_rect.right
        max_y = self.screen_rect.bottom
        if self.moving_right and new_rect.right + self.settings.ship_speed <= max_x:
            new_rect.x += self.settings.ship_speed
        if self.moving_left and new_rect.left - self.settings.ship_speed >= min_x:
            new_rect.x -= self.settings.ship_speed
        if self.moving_up and new_rect.top - self.settings.ship_speed >= 0:
            new_rect.y -= self.settings.ship_speed
        if self.moving_down and new_rect.bottom + self.settings.ship_speed <= max_y:
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












