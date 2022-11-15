import json
import pygame
from pygame import Vector2
from settings import TILESIZE
from sprites.player import Player
from sprites.platform import Platform
from states.state import State
from camera import Camera



class Level(State):
    def __init__(self, game):
        super().__init__(game)
        self.all_sprites = Camera(self.game, self)
        self.platform_group = pygame.sprite.Group()
        self.spike_group = pygame.sprite.Group()
        self.spawn = pygame.sprite.GroupSingle()
        self.finish_group = pygame.sprite.Group()



        self.player = pygame.sprite.GroupSingle(
            Player(Vector2(100, 100), self.game, self, self.all_sprites)
        )

        self.level_file = "../assets/levels/level-1.json"

        self.load_level()

    def update(self, delta_time, keys):
        self.player.update(delta_time, keys)
        self.platform_group.update(delta_time, keys)


    def render(self):
        self.game.game_canvas.fill((0,0,0))
        self.all_sprites.draw(self.player.sprite.rect.center)


    def load_level(self):
        with open(self.level_file, "r") as file:
            level_data = json.load(file)

        height = level_data["height"]
        width = level_data["width"]

        for layer in level_data["layers"]:
            if layer["name"] == "Platform":
                for i in range((height * width) - 1):
                    if layer["data"][i] != 0:
                        Platform(
                            Vector2((i % width) * TILESIZE, (i // width) * TILESIZE),
                            self.game,
                            self,    
                            self.all_sprites, 
                            self.platform_group
                        )