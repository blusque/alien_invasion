import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """初始化按钮属性"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.screen_rect = screen.get_rect()
        self.button_size = ai_settings.button_size
        self.button_color = ai_settings.button_color
        self.text_color = ai_settings.text_color
        self.font = pygame.font.SysFont(None, 48)
        
        #创建按钮的rect对象并使其居中
        self.rect = pygame.Rect(0, 0, self.button_size[0], self.button_size[1])
        self.rect.center = self.screen_rect.center

        #按钮的标签
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class SButton(Button):
    def __init__(self, ai_settings, screen, msg, button_size, button_color, rect_x, rect_y, font_size):
        super().__init__(ai_settings, screen, msg)
        self.rect = pygame.Rect(0, 0, button_size[0], button_size[1])
        self.rect.center = rect_x, rect_y
        self.font = pygame.font.SysFont(None, font_size)
        self.button_size = button_size
        self.button_color = button_color

        self.prep_msg(msg)
