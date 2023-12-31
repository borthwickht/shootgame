import pygame
import sys

from game_parameters import *
from junk import *
from background import draw_background, add_notebook, add_bottle, add_salt, add_duck
from players import Player, Player2
from ducks import Duck, ducks


# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shoot only the ducks')

# clock object
clock = pygame.time.Clock()

# Main Loop
running = True
background = screen.copy()
draw_background(background)

# add bottle
add_bottle(3)

# add salt
add_salt(3)

# add notebook
add_notebook(3)

# add ducks
add_duck(5)

# create both players
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
player2 = Player2(SCREEN_WIDTH/2 - TILE_SIZE, SCREEN_HEIGHT/2 - TILE_SIZE)

# initialize score for shoot game
score1 = 0
score2 = 0
score_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 48)

# load the sound effects
duck_hit = pygame.mixer.Sound("assets/sounds/boom_x.wav")
bottle_hit = pygame.mixer.Sound("assets/sounds/glass_shatter_c.wav")
notebook_hit = pygame.mixer.Sound("assets/sounds/paper_tearing.wav")
salt_hit = pygame.mixer.Sound("assets/sounds/metal_crunch.wav")
done = pygame.mixer.Sound("assets/sounds/buzzer_x.wav")
pygame.mixer.music.load("assets/sounds/enchanted-chimes.mp3")

# play background music
pygame.mixer.music.play(-1)

# set time limit
time_limit = 20

# get initial time
start_time = pygame.time.get_ticks() / 1000 # convert to seconds because get_ticks is milliseconds

# set up time to switch between target and explosion images
switch_time = 500
last_switch_time = pygame.time.get_ticks()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # control players with keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_w:
                player2.move_up()
            if event.key == pygame.K_s:
                player2.move_down()
            if event.key == pygame.K_a:
                player2.move_left()
            if event.key == pygame.K_d:
                player2.move_right()

            # check for player1 shooting duck
            for duck in ducks:
                if event.key == pygame.K_m:
                    player.switch_image()  # switch image when the player shoots
                    hit = pygame.sprite.spritecollide(player, ducks, True)
                    if hit:
                        pygame.mixer.Sound.play(duck_hit)
                        score1 += 1
                        add_duck(len(hit))
            # check for player 1 shooting bottle
            for bottle in bottles:
                if event.key == pygame.K_m:
                    player.switch_image()  # switch image when the player shoots
                    miss1 = pygame.sprite.spritecollide(player, bottles, True)
                    if miss1:
                        pygame.mixer.Sound.play(bottle_hit)
                        score1 -= 1
                        add_bottle(len(miss1))
            # check for player 1 shooting salt
            for salt in salts:
                if event.key == pygame.K_m:
                    player.switch_image()  # switch image when the player shoots
                    miss2 = pygame.sprite.spritecollide(player, salts, True)
                    if miss2:
                        pygame.mixer.Sound.play(salt_hit)
                        score1 -= 1
                        add_salt(len(miss2))
            # check for player 1 shooting notebook
            for notebook in notebooks:
                if event.key == pygame.K_m:
                    player.switch_image()  # switch image when the player shoots
                    miss3 = pygame.sprite.spritecollide(player, notebooks, True)
                    if miss3:
                        pygame.mixer.Sound.play(notebook_hit)
                        score1 -= 1
                        add_notebook(len(miss3))

            # check for player2 shooting duck
            for duck in ducks:
                if event.key == pygame.K_c:
                    player2.switch_image()  # switch image when the player shoots
                    hit = pygame.sprite.spritecollide(player2, ducks, True)
                    if hit:
                        pygame.mixer.Sound.play(duck_hit)
                        score2 += 1
                        add_duck(len(hit))
            # check for player 2 shooting bottle
            for bottle in bottles:
                if event.key == pygame.K_c:
                    player2.switch_image()  # switch image when the player shoots
                    miss1 = pygame.sprite.spritecollide(player2, bottles, True)
                    if miss1:
                        pygame.mixer.Sound.play(bottle_hit)
                        score2 -= 1
                        add_bottle(len(miss1))
            # check for player 2 shooting salt
            for salt in salts:
                if event.key == pygame.K_c:
                    player2.switch_image()  # switch image when the player shoots
                    miss2 = pygame.sprite.spritecollide(player2, salts, True)
                    if miss2:
                        pygame.mixer.Sound.play(salt_hit)
                        score2 -= 1
                        add_salt(len(miss2))
            # check for player 2 shooting salt
            for notebook in notebooks:
                if event.key == pygame.K_c:
                    player2.switch_image()  # switch image when the player shoots
                    miss3 = pygame.sprite.spritecollide(player2, notebooks, True)
                    if miss3:
                        pygame.mixer.Sound.play(notebook_hit)
                        score2 -= 1
                        add_notebook(len(miss3))

    # draw background
    screen.blit(background, (0, 0))

    # draw bottles
    bottles.update()

    # draw notebook
    notebooks.update()

    # draw salt
    salts.update()

    # draw player1 target
    player.update()

    # draw player2 target
    player2.update()

    # draw ducks
    ducks.update()

    # check if any salt is off the screen
    for salt in salts:
        if salt.rect.x < -salt.rect.width:  # use the tile size
            salts.remove(salt)  # remove the salt from the sprite group
            add_salt(1)

    # check if any bottle is off the screen
    for bottle in bottles:
        if bottle.rect.x < -bottle.rect.width:  # use the tile size
            bottles.remove(bottle)  # remove the bottle from the sprite group
            add_bottle(1)

        # check if any notebook is off the screen
        for notebook in notebooks:
            if notebook.rect.x < -notebook.rect.width:  # use the tile size
                notebooks.remove(notebook)  # remove the notebook from the sprite group
                add_notebook(1)

        for duck in ducks:
            if duck.rect.y > SCREEN_WIDTH:  # use the tile size
                ducks.remove(duck)  # remove the duck from the sprite group
                add_duck(1)

    # draw game objects
    bottles.draw(screen)
    notebooks.draw(screen)
    salts.draw(screen)
    player.draw(screen)
    player2.draw(screen)
    ducks.draw(screen)

    # draw the scores on the screen
    player1_score = score_font.render(f"{score1}", True, (255, 0, 0))
    screen.blit(player1_score, (SCREEN_WIDTH - TILE_SIZE, 0))
    player2_score = score_font.render(f"{score2}", True, (255, 0, 0))
    screen.blit(player2_score, (0 + TILE_SIZE, 0))

    # get current time and draw on screen
    current_time = pygame.time.get_ticks() / 1000  # convert to seconds
    display_time = score_font.render(f"{current_time}", True, (255, 0, 0))
    screen.blit(display_time, ((SCREEN_WIDTH / 2) - 55, TILE_SIZE))

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

    # check if the time limit is reached
    elapsed_time = current_time - start_time
    if elapsed_time >= time_limit:
        running = False

# create new background when game over
screen.blit(background, (0, 0))

# show game over message
message = score_font.render("GAME OVER", True, (0, 0, 0))
screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2))

# show final score
if score1 > score2:
    score_text = score_font.render(f"Player 1 wins {score1} to {score2}", True, (0, 0, 255))
    screen.blit(score_text,
            (SCREEN_WIDTH / 2 - score_text.get_width() / 2, SCREEN_HEIGHT / 2 + score_text.get_height()))
else:
    score_text = score_font.render(f"Player 2 wins {score2} to {score1}", True, (0, 0, 255))
    screen.blit(score_text,
            (SCREEN_WIDTH / 2 - score_text.get_width() / 2, SCREEN_HEIGHT / 2 + score_text.get_height()))
# update display
pygame.display.flip()

# play game over sound effect
pygame.mixer.Sound.play(done)

# wait for user to exit the game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit pygame
            pygame.quit()
            sys.exit()

# TODO
    # helped Justin with capping his frame rate so the enemies only shoot once a second
    # Justin helped me with setting up the timer