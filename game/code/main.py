import pygame
from pygame import Vector2
import os
import sys
from settings import *
from time import time
from states.level import Level
from states.start_menu import StartMenu
from debug import Debug


class Game:
    def __init__(self):
        pygame.init()
        self.game_canvas = pygame.Surface((GAME_W, GAME_H))
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()
        self.dt, self.prev_time = 0, time()

        self.show_debug = False


        self.state_stack = []

        self.load_assets()
        self.load_state()

        self.debug = Debug(self)  


    def run(self):
        while True:
            self.print_debug()

            self.get_dt()
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)


    def print_debug(self):
        self.debug.print(f"FPS: {int(self.clock.get_fps())}")
        self.debug.print(f"DeltaTime: {self.dt:0.5f}")

    def handle_events(self):
        self.keys = pygame.key.get_pressed()
        self.events = pygame.event.get()

        self.mouse_pressed = pygame.mouse.get_pressed()
        self.mouse_pos = Vector2(pygame.mouse.get_pos()) / SCALE
        
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    self.show_debug = not self.show_debug    

    def render(self):
        self.game_canvas.fill((0,0,0))
        self.state_stack[-1].render()

        if self.show_debug:
            self.debug.draw()
        else:
            self.debug.clear()

        scaled_canvas = pygame.transform.scale(self.game_canvas, (SCREEN_W, SCREEN_H))

        self.screen.blit(scaled_canvas, (0, 0))
        pygame.display.update()

    def update(self):
        if self.state_stack:
            self.state_stack[-1].update(self.dt, self.keys)

    def get_dt(self):
        self.dt = (time() - self.prev_time)
        self.prev_time = time()
        return self.dt

    def load_state(self):
        start_menu = Level(self)
        self.state_stack.append(start_menu)
    
    def load_assets(self):
        self.font_dir = "../assets/fonts/"
        self.default_font_path = os.path.join(self.font_dir, "PressStart2P-Regular.ttf")
        self.default_font = pygame.font.Font(self.default_font_path, 18)

    def draw_text(self, text, pos, font=None, color=(255,255,255)):
        if font is None:
            font = self.default_font
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = pos
        self.game_canvas.blit(text_surface, text_rect)



if __name__ == "__main__":
    game = Game()
    game.run()