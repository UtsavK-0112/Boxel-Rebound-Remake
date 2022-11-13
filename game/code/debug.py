import pygame
from pygame import Vector2
from settings import *

class Debug:
    def __init__(self, game):
        self.game = game
        self.game.game_canvas
        self.font = pygame.font.Font(self.game.default_font_path, 8)

        self.text_color = (255, 255, 255)
        self.background_color = (110, 110, 110)
        self.background_alpha = 128

        self.margin = (0, 0)
        self.padding = (4, 4)
        self.line_height = 5
        self.spacing = 0

        self.pos = Vector2(self.margin)

        self.text_surfaces = pygame.surface.Surface((GAME_W, GAME_H))
        self.text_surfaces.set_colorkey((0, 0, 0))

        self.background_surfaces = pygame.surface.Surface((GAME_W, GAME_H))
        self.background_surfaces.set_colorkey((0, 0, 0))


    
    def print(self, *text, align="left"):
        for line in text:
            if line == "":
                self.pos += Vector2(0, self.line_height + self.spacing + self.padding[1] * 2)
                continue

            text_surface = self.font.render(str(line), False, self.text_color)
            text_rect = text_surface.get_rect(topleft = self.pos)
            text_rect.width += self.padding[0] * 2
            text_rect.height += self.padding[1] * 2

            pygame.draw.rect(self.background_surfaces, self.background_color, text_rect)
            self.text_surfaces.blit(text_surface, self.pos + Vector2(self.padding) + Vector2(0,2))

            self.pos += Vector2(0, self.line_height + self.spacing + self.padding[1] * 2)

    def draw(self):
        self.background_surfaces.set_alpha(self.background_alpha)
        self.game.game_canvas.blit(self.background_surfaces, (0, 0))
        self.game.game_canvas.blit(self.text_surfaces, (0, 0))
        self.pos = Vector2(self.margin)
        self.clear()

    def clear(self):
        self.text_surfaces.fill((0, 0, 0))
        self.background_surfaces.fill((0, 0, 0))

            

