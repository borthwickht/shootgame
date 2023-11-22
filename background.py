import pygame
from game_parameters import *
import random
from junk import Bottle, bottles, Notebook, notebooks, Salt, salts
from ducks import Duck, ducks

def draw_background(screen):
    #load our tiles
    grass = pygame.image.load("assets/sprites/grass.png").convert()
    sand = pygame.image.load("assets/sprites/sand.png").convert()
    dirt = pygame.image.load("assets/sprites/dirt.png").convert()

    #use png transparency
    sand.set_colorkey((0,0,0))
    grass.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0,SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(dirt, (x,y))

        # draw the sandy bottom
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            screen.blit(sand, (x, SCREEN_HEIGHT - TILE_SIZE))

    #- add grass randomly on the screen
    for _ in range(7):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0,SCREEN_HEIGHT)
        screen.blit(grass,(x,y-TILE_SIZE*2))

    # draw the text
    custom_font = pygame.font.Font('assets/Fonts/28 Days Later.ttf', 64)
    text = custom_font.render('Shoot', True, (255,0,0))
    screen.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2,SCREEN_HEIGHT/17 - text.get_height()/2))

def add_bottle(num_bottle):
    for _ in range(num_bottle):
        bottles.add(Bottle(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 1.5),
                    random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

def add_notebook(num_notebook):
    for _ in range(num_notebook):
        notebooks.add(Notebook(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 1.5),
                    random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

def add_salt(num_salt):
    for _ in range(num_salt):
        salts.add(Salt(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 1.5),
                    random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

def add_duck(num_duck):
    for _ in range(num_duck):
        ducks.add(Duck(random.randint(0 + TILE_SIZE/2, SCREEN_WIDTH - TILE_SIZE/2),
                       random.randint(-128, -64)))