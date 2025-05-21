import pygame
import pygame.font

class Scoreboard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (0, 0 , 0)
        self.font = pygame.font.SysFont(None, 36)

        self.score1 = 0
        self.score2 = 0

        self.prep_scores()

    def prep_scores(self):
        score1_str = f"Player 1: {self.score1}"
        self.score1_image = self.font.render(score1_str, True, self.text_color, None)
        self.score1_rect = self.score1_image.get_rect()
        self.score1_rect.left = 10
        self.score1_rect.top = 20

        
        score2_str = f"Player 2: {self.score2}"
        self.score2_image = self.font.render(score2_str, True, self.text_color, None)
        self.score2_rect = self.score2_image.get_rect()
        self.score2_rect.right = self.screen_rect.right - 20
        self.score2_rect.top = 20

    def show_scores(self):
        self.screen.blit(self.score1_image, self.score1_rect)
        self.screen.blit(self.score2_image, self.score2_rect)

    def increase_score1(self, amount):
        self.score1 += amount
        self.prep_scores()

    def increase_score2(self, amount):
        self.score2 += amount
        self.prep_scores()
