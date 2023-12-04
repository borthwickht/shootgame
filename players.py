import pygame
from game_parameters import *
# from event import *

# create a pygame sprite class for both players to use

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/crosshair_blue_small.png')
        self.boom_image1 = pygame.image.load('assets/sprites/tank_explosion4.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0
        self.current_image = self.image
        self.switch_duration = 100
        self.last_switch_time = 0

    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED

    def move_right(self):
        self.x_speed = PLAYER_SPEED

    def stop(self):
        self.y_speed = 0
        self.x_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > SCREEN_WIDTH - TILE_SIZE:
            self.x = SCREEN_WIDTH-TILE_SIZE
            self.x_speed = 0
        if self.x < 0:
            self.x = 0
            self.x_speed = 0
        if self.y > SCREEN_HEIGHT - (2*TILE_SIZE):
            self.y = SCREEN_HEIGHT -(2*TILE_SIZE)
            self.y_speed = 0
        if self.y < 0:
            self.y = 0
            self.y_speed = 0
        self.rect.x = self.x
        self.rect.y = self.y
        if pygame.time.get_ticks() - self.last_switch_time >= self.switch_duration:
            self.current_image = self.image

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)

    def switch_image(self):
        self.current_image = self.boom_image1
        self.last_switch_time = pygame.time.get_ticks()

class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/crosshair_red_small.png')
        self.boom_image2 = pygame.image.load('assets/sprites/tank_explosion4.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0
        self.current_image = self.image
        self.switch_duration = 100
        self.last_switch_time = 0

    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED

    def move_right(self):
        self.x_speed = PLAYER_SPEED

    def stop(self):
        self.y_speed = 0
        self.x_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > SCREEN_WIDTH - TILE_SIZE:
            self.x = SCREEN_WIDTH-TILE_SIZE
            self.x_speed = 0
        if self.x < 0:
            self.x = 0
            self.x_speed = 0
        if self.y > SCREEN_HEIGHT - (2*TILE_SIZE):
            self.y = SCREEN_HEIGHT -(2*TILE_SIZE)
            self.y_speed = 0
        if self.y < 0:
            self.y = 0
            self.y_speed = 0
        self.rect.x = self.x
        self.rect.y = self.y
        if pygame.time.get_ticks() - self.last_switch_time >= self.switch_duration:
            self.current_image = self.image

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)

    def switch_image(self):
        self.current_image = self.boom_image2
        self.last_switch_time = pygame.time.get_ticks()

