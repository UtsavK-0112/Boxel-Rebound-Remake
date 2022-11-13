import pygame
from pygame import Vector2
from settings import *
from states.state import State
from states.level import LevelSelect
from button import Button


class StartMenu(State):
    def __init__(self, game):
        super().__init__(game)

        self.level_select = LevelSelect(self.game)

        self.start_button = Button(GAME_W / 2, GAME_H / 2, "Start", lambda: self.level_select.enter_state(), self.game)

    def update(self, dt, keys):
        self.start_button.update()

    def render(self):
        self.game.game_canvas.fill((0,255,0))
        self.start_button.render()

        self.game.draw_text("Main Menu", (GAME_W/2, GAME_H//5))


