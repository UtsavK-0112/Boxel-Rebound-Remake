import pygame
from pygame import Vector2



class Button(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, text: str, onclick: object, game, width=None, height=None, background_color=(173, 78, 228), text_color=(255,255,255)):
        super().__init__()
        self.width = width
        self.height = height

        self.game = game
        self.font = game.default_font
        self.text = text
        self.pos = Vector2(x, y)

        self.colors = {
            "text": text_color,
            "background": background_color,
            "text_hover": (0,0,0),
            "background_hover": (255,255,255)
        }

        self.text_color = text_color
        self.background_color = background_color


        self.set_text(self.text)

        self.hovered = False
        self.onclick = onclick

    def update(self):
        self.check_for_hover()
        if self.hovered:
            self.background_color = self.colors["background_hover"]
            self.text_color = self.colors["text_hover"]
        else:
            self.background_color = self.colors["background"]
            self.text_color = self.colors["text"]

        if self.hovered and self.game.mouse_pressed[0]:
            for event in self.game.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.onclick()

    def render(self):
        pygame.draw.rect(self.game.game_canvas, self.background_color, self.background_rect)
        self.text_surface = self.font.render(self.text, False, self.text_color)
        self.game.game_canvas.blit(self.text_surface, self.rect)

    def check_for_hover(self):
        self.hovered = self.background_rect.collidepoint(self.game.mouse_pos)
        self.game.debug.print(f"Mouse Pos: {self.game.mouse_pos}")
        self.game.debug.print(f"Button hovered: {self.hovered}")

    def set_text(self, text: str):
        self.text = text
        self.text_surface = self.font.render(self.text, False, self.text_color)
        self.rect: pygame.rect.Rect = self.text_surface.get_rect()


        self.background_rect = self.rect.copy()

        if self.width:
            self.background_rect.width = self.width
        
        if self.height:
            self.background_rect.height = self.height

        self.background_rect = self.background_rect.inflate(10, 10)

        
        self.rect.center = self.pos
        self.background_rect.center = self.pos
