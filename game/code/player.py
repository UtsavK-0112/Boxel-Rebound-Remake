import pygame
from pygame import Vector2



class Player(pygame.sprite.Sprite):
    def __init__(self, pos: Vector2, game, level, *groups):
        super().__init__(groups)
        self.game = game
        self.level = level

        self.sprite_rotation = 0
        self.sprite_scale = 1

        self.main_sprite = pygame.image.load("../assets/images/Player.png").convert_alpha()
        self.main_sprite = pygame.transform.scale(self.main_sprite, (int(self.main_sprite.get_width() * self.sprite_scale), int(self.main_sprite.get_height() * self.sprite_scale)))

        
        self.image = pygame.transform.rotate(self.main_sprite, self.sprite_rotation)

        self.pos = pos
        self.vel = Vector2(0, 0)
        self.rect = self.image.get_rect(topleft = self.pos)

        self.speed = 100
        self.friction = 0.9
        self.jump_power = 10000
        self.gravity = 200
        self.terminal_y_vel = 300



    def update(self, delta_time, keys):
        self.input(delta_time, keys)
        self.image = pygame.transform.rotate(self.main_sprite, self.sprite_rotation)

        self.apply_gravity(delta_time)
        self.apply_friction(delta_time)
        self.pos += self.vel * delta_time
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        self.game.debug.print(f"Player pos: {self.pos}")
        self.game.debug.print(f"Player vel: {self.vel}")


    def apply_friction(self, delta_time):
        self.vel.x *= 1/(1 + (self.friction * delta_time))



    def input(self, delta_time, keys):
        for event in self.game.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     self.vel.y = -self.jump_power * delta_time
            
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vel.x = -self.speed * delta_time
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vel.x = self.speed * delta_time


    def apply_gravity(self, delta_time):
        if self.vel.y < self.terminal_y_vel:
            self.vel.y += self.gravity * delta_time
        else:
            self.vel.y = self.terminal_y_vel

        

