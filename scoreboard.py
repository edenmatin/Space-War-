import pygame
import pygame.font

class Scoreboard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color1 = (0,180, 255)   
        self.text_color2 = (0, 0, 0)   

        self.font = pygame.font.SysFont(None, 36)

        self.score1 = 0
        self.score2 = 0

        self.prep_scores()

    def prep_scores(self):
        self.player1_image = self.font.render("Player 1", True, self.text_color1)
        self.player1_rect = self.player1_image.get_rect()
        self.player1_rect.left = 10
        self.player1_rect.top = 5 

      
        score1_str = f"Score: {self.score1}"
        self.score1_image = self.font.render(score1_str, True, self.text_color1)
        self.score1_rect = self.score1_image.get_rect()
        self.score1_rect.left = self.player1_rect.left
        self.score1_rect.top = self.player1_rect.bottom + 2

       
        self.player2_image = self.font.render("Player 2", True, self.text_color2)
        self.player2_rect = self.player2_image.get_rect()
        self.player2_rect.right = self.screen_rect.right - 20
        self.player2_rect.top = 5 

        score2_str = f"Score: {self.score2}"
        self.score2_image = self.font.render(score2_str, True, self.text_color2)
        self.score2_rect = self.score2_image.get_rect()
        self.score2_rect.right = self.player2_rect.right
        self.score2_rect.top = self.player2_rect.bottom + 2


    def show_scores(self):
        self.screen.blit(self.player1_image, self.player1_rect)
        self.screen.blit(self.score1_image, self.score1_rect)
        self.screen.blit(self.player2_image, self.player2_rect)
        self.screen.blit(self.score2_image, self.score2_rect)

    def increase_score1(self, amount):
        self.score1 += amount
        self.prep_scores()

    def increase_score2(self, amount):
        self.score2 += amount
        self.prep_scores()
