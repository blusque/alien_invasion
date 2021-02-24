import pygame as pg


class Bar():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pg.Rect(0, 0, 1210, 45)
        self.rect.x = -5
        self.rect.y = -5
        self.color = 230, 230, 230

    def bar_draw(self):
        self.screen.fill(self.color, self.rect)

class ScoreBoard():
    def __init__(self, ai_settings, stats, rect= (1170, 10) , screen = None):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.right = rect[0]
        self.top = rect[1]
        

        self.text_color = 30, 30, 30
        self.bg_color = 230, 230, 230
        self.font = pg.font.SysFont(None, ai_settings.score_font_size)

        self.prep_scoreboard()

    def prep_scoreboard(self):
        score_int = int(round(self.stats.score, -1))
        score_str = "{:,}".format(score_int)
        self.score_img = self.font.render(score_str, True, self.text_color,
        self.bg_color)

        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.top = self.top
        self.score_img_rect.right = self.right

    def show_score(self):
        self.screen.blit(self.score_img, self.score_img_rect)
