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

        self.speed = 7500
        self.friction = 10
        self.jump_power = 20000
        self.gravity = 1000
        self.terminal_y_vel = 300



    def update(self, delta_time, keys):
        self.input(delta_time, keys)
        self.image = pygame.transform.rotate(self.main_sprite, self.sprite_rotation)

        self.apply_gravity(delta_time)
        self.apply_friction(delta_time)

        self.collisions(self.level.all_sprites)

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


    def collisions(self, all_sprites: pygame.sprite.Group):
        self.collision_dict = {
            'top': [],
            'bottom': [],
            'left': [],
            'right': []
        }

        self.pos.y += self.vel.y * self.game.dt
        self.rect.y = round(self.pos.y)


        for sprite in all_sprites.sprites():
            if sprite == self:
                continue
            
            for hitbox in sprite.hitbox:
                if hitbox.colliderect(self.rect):
                    if self.vel.y > 0:
                        self.collision_dict['bottom'].append(sprite)
                        if sprite.collidable:
                            self.rect.bottom = hitbox.top
                            self.vel.y = 0
                    elif self.vel.y < 0:
                        self.collision_dict['top'].append(sprite)
                        if sprite.collidable:
                            self.rect.top = hitbox.bottom
                            self.vel.y = 0

        self.pos.y = self.rect.y
        

        self.pos.x += self.vel.x * self.game.dt
        self.rect.x = round(self.pos.x)

        for sprite in all_sprites.sprites():
            if sprite == self:
                continue
            
            for hitbox in sprite.hitbox:
                if hitbox.colliderect(self.rect):
                    if self.vel.x > 0:
                        self.collision_dict['right'].append(sprite)
                        if sprite.collidable:
                            self.rect.right = hitbox.left
                            self.vel.x = 0
                    elif self.vel.x < 0:
                        self.collision_dict['left'].append(sprite)
                        if sprite.collidable:
                            self.rect.left = hitbox.right
                            self.vel.x = 0

        self.pos.x = self.rect.x
