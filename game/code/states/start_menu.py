import pygame
from pygame import Vector2
from settings import *
from states.state import State
from states.level_select import LevelSelect
from states.options import Options
from states.rules import Rules
from button import Button


class StartMenu(State):
    def __init__(self, game):
        super().__init__(game)

        self.button_group = pygame.sprite.Group(
            Button(GAME_W / 2, GAME_H / 2 - 50, "Start", lambda: self.load_state(LevelSelect), self.game, 150),
            Button(GAME_W / 2, GAME_H / 2, "Options", lambda: self.load_state(Options), self.game, 150),
            Button(GAME_W / 2, GAME_H / 2 + 50, "Help", lambda: self.load_state(Rules), self.game, 150)
        )
        


    def update(self, dt, keys):
        self.button_group.update()

    def render(self):
        self.game.game_canvas.fill((206, 94, 243))
        for button in self.button_group.sprites():
            button.render()

        self.game.draw_text("Main Menu", (GAME_W/2, GAME_H//5))

    def load_state(self, state):
        self.next_state = state(self.game)
        self.next_state.enter_state()



