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

        scoreboard_height = 60
        min_x = 0
        max_x = self.screen_rect.right
        max_y = self.screen_rect.bottom


        in_scoreboard_x_range = (0 <= new_rect.left <= 110) or (1390 <= new_rect.right <= 1500)

        # اگر کشتی در محدوده x مربوط به scoreboard است، محدودیت y اعمال می‌شود
        if in_scoreboard_x_range:
            # جلوگیری از ورود به y < scoreboard_height
            # یعنی اگر حرکت به بالا باعث بشه از y=100 کمتر بشه، اجازه نده
            if self.moving_up and new_rect.top - self.settings.ship_speed < scoreboard_height:
                pass  # حرکت بالا ممنوع
            elif self.moving_up:
                new_rect.y -= self.settings.ship_speed

            # حرکت به پایین آزاد است (تا پایین صفحه)
            if self.moving_down and new_rect.bottom + self.settings.ship_speed <= max_y:
                new_rect.y += self.settings.ship_speed

            # حرکت افقی فقط اگر موقعیت y کشتی داخل scoreboard نباشد مجاز است
            # یعنی فقط زمانی که y کشتی >= scoreboard_height هست حرکت افقی داشته باشیم
            if new_rect.top >= scoreboard_height:
                if self.moving_right and new_rect.right + self.settings.ship_speed <= max_x:
                    new_rect.x += self.settings.ship_speed
                if self.moving_left and new_rect.left - self.settings.ship_speed >= min_x:
                    new_rect.x -= self.settings.ship_speed
        else:
            # اگر کشتی در محدوده x کناره‌ها نیست، حرکت آزاد است
            if self.moving_right and new_rect.right + self.settings.ship_speed <= max_x:
                new_rect.x += self.settings.ship_speed
            if self.moving_left and new_rect.left - self.settings.ship_speed >= min_x:
                new_rect.x -= self.settings.ship_speed
            if self.moving_up and new_rect.top - self.settings.ship_speed >= 0:
                new_rect.y -= self.settings.ship_speed
            if self.moving_down and new_rect.bottom + self.settings.ship_speed <= max_y:
                new_rect.y += self.settings.ship_speed

        # جلوگیری از برخورد با دیوارها
        for wall in self.ai_game.walls:
            if new_rect.colliderect(wall.rect):
                return

        # جلوگیری از برخورد با کشتی دیگر
        if new_rect.colliderect(other_ship.rect):
            return

        # به‌روزرسانی موقعیت کشتی
        self.rect = new_rect
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)









