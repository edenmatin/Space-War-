import pygame
from wall import Wall 

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # اندازه پنجره
        pygame.display.set_caption("Wall Demo")

        self.wall_group = pygame.sprite.Group()
        self.create_wall()

    def create_wall(self):
        # ساخت یک آجر نمونه برای گرفتن اندازه
        temp_brick = Wall(self, 0, 0)
        brick_width = temp_brick.rect.width
        brick_height = temp_brick.rect.height

        # محاسبه مکان x برای مرکز افقی
        screen_rect = self.screen.get_rect()
        center_x = screen_rect.centerx - (brick_width // 2)

        # ساخت 3 آجر عمودی
        for i in range(3):
            y = i * brick_height  # مکان y برای هر آجر
            brick = Wall(self, center_x, y)
            self.wall_group.add(brick)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))  # پس‌زمینه سفید
            self.wall_group.draw(self.screen)  # رسم دیوار
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
