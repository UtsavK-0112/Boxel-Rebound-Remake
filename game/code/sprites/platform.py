import pygame
from pygame import Vector2


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos: Vector2, game, level, *groups):
        super().__init__(groups)
        self.game = game
        self.level = level

        self.sprite_rotation = 0
        self.sprite_scale = 1

        self.main_sprite = pygame.image.load("../assets/images/Platform.png").convert_alpha()
        self.main_sprite = pygame.transform.scale(self.main_sprite, (int(self.main_sprite.get_width() * self.sprite_scale), int(self.main_sprite.get_height() * self.sprite_scale)))
        self.image = pygame.transform.rotate(self.main_sprite, self.sprite_rotation)

        self.pos = pos
        self.rect = self.image.get_rect(topleft = self.pos)

        self.collidable = True
        self.hitbox = [self.rect.copy()]
