# create a class for different distractions

import pygame
import random
from game_parameters import *

class Bottle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/bottle.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_JUNK_SPEED, MAX_JUNK_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image, self.rect)

bottles = pygame.sprite.Group()

class Notebook(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/notebook.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_JUNK_SPEED, MAX_JUNK_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image, self.rect)

notebooks = pygame.sprite.Group()

class Salt(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/salt.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_JUNK_SPEED, MAX_JUNK_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image, self.rect)

salts = pygame.sprite.Group()