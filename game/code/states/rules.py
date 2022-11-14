import pygame
from pygame import Vector2
from settings import *
from states.state import State
from button import Button


class Rules(State):
    def __init__(self, game):
        super().__init__(game)

        self.button_group = pygame.sprite.Group(
        Button(GAME_W / 2, GAME_H / 2, "Back", lambda: self.exit_state(), self.game)
        )

    def update(self, delta_time, keys):
        self.button_group.update()

    def render(self):
        self.game.game_canvas.fill((255,255,0))
        for button in self.button_group.sprites():
            button.render()
        self.game.draw_text("How to Play", (GAME_W/2, GAME_H//5))
