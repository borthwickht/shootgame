# create a class for the target ducks

import pygame
import random
from game_parameters import *

class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/duck_brown.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_JUNK_SPEED, MAX_JUNK_SPEED)
        self.rect.center = (x,y)

    def update(self, new =0):
        self.y += self.speed + new
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)

ducks = pygame.sprite.Group()