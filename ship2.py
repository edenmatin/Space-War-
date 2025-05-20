import pygame
class Ship2:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("./images/rocket2.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect) 
    def update2(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship2_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship2_speed
        self.rect.x = self.x