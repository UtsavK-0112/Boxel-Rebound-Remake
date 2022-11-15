import pygame
from pygame import Vector2
from settings import *


class Camera(pygame.sprite.Group):
    def __init__(self, game, level, *sprites):
        super().__init__(sprites)
        self.game = game
        self.level = level


    def draw(self, player_position):
        offset = player_position - Vector2(GAME_W / 2, GAME_H / 2)
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.topleft -= offset
            
            if hasattr(sprite, 'draw'):
                sprite.draw(self.game.game_canvas, offset)
            else:
                self.game.game_canvas.blit(sprite.image, offset_rect)
