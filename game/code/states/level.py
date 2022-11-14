import pygame
from pygame import Vector2
from states.state import State
from player import Player


class Level(State):
    def __init__(self, game):
        super().__init__(game)
        self.all_sprites = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle(
            Player(Vector2(100, 100), self.game, self, self.all_sprites)
        )

        self.level_file = "../assets/levels/level_1.txt"

    def update(self, delta_time, keys):
        self.player.update(delta_time, keys)


    def render(self):
        self.game.game_canvas.fill((0,0,0))
        self.all_sprites.draw(self.game.game_canvas)


    def load_level(self):
        pass