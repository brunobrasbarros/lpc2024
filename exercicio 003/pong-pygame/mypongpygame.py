#Jucimar Jr
#2024

#Bruno Brás Barros
#2415310041

import pygame
import random

pygame.init()

#game colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

#score selection by the user
score_select = int(input("select the max points for the victory condition: "))
SCORE_MAX = score_select

#game screen
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2024-09-02")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
player_2_y = 300

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 2.5
ball_dy = 2.5
ball_speed = 2.5
initial_ball_speed = 2.5

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

#selecting and playing the sountrack
soundtrack_list =\
["SOUNDTRACKS/Mega Man 2 - Dr. Wily's Castle - UryaV.mp3",
"SOUNDTRACKS/DuckTales Music (NES) - The Moon Theme - explod2A03.mp3",
"SOUNDTRACKS/Masked Dedede 8 Bit Remix - Kirby Super Star Ultra (Konami VRC6) - Bulby.mp3",
"SOUNDTRACKS/Castlevania II Music (NES) - Bloody Tears (Day Theme) - explod2A03.mp3",
"SOUNDTRACKS/Undertale Ost_ 087 - Hopes and Dreams - Misaki.mp3"
 ]

soundtrack_selection = random.choice(soundtrack_list)
soundtrack = pygame.mixer.Sound(soundtrack_selection)

soundtrack.set_volume(0.3)
soundtrack.play()

#the game

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        # keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 690:
            ball_dy *= -1
            bounce_sound_effect.play()

        elif ball_y <= 10:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1's paddle
        if 100 > ball_x > 50:
            if player_1_y < ball_y + 50 and player_1_y + 175 > ball_y:
                ball_dx *= -1.0

                # ball's impact point
                impact_point = ball_y - player_1_y

                offset = impact_point - 75  #  paddle's center

                # angle and speed adjustment
                ball_dy += offset * 0.02

                ball_speed = min(ball_speed + 0.2, 4)

                bounce_sound_effect.play()

        # ball collision with the player 2's paddle
        if 1160 < ball_x < 1200:
            if player_2_y < ball_y + 25 and player_2_y + 150 > ball_y:
                ball_dx *= -1

                # ball's impact point
                impact_point = ball_y - player_2_y
                offset = impact_point - 75  # paddle's center

                # angle and speed adjustment
                ball_dy += offset * 0.02
                ball_speed = min(ball_speed + 0.2, 4)
                bounce_sound_effect.play()

        # scoring points
        if ball_x < 0:
            ball_x = 640
            ball_y = 360
            ball_dy = 2.1
            ball_dx = 2.1
            ball_speed = 2.1
            ball_speed = initial_ball_speed
            score_2 += 1
            scoring_sound_effect.play()
        elif ball_x > 1280:
            ball_x = 640
            ball_y = 360
            ball_dy = 2.1
            ball_dx = 2.1
            ball_speed = 2.1
            ball_speed = initial_ball_speed
            score_1 += 1
            scoring_sound_effect.play()

        # ball movement
        ball_x += ball_dx * ball_speed
        ball_y += ball_dy * ball_speed

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 5
        if player_1_move_down:
            player_1_y += 5

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # player 2 "Artificial Intelligence"
        if ball_x > 640:
            if player_2_y + 75 < ball_y:
                player_2_y += random.randint(4, 5)
            elif player_2_y + 75 > ball_y:
                player_2_y -= random.randint(4, 5)

        #player 2 paddle returning to the original place
        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 570:
            player_2_y = 570

        # update score hud
        score_text = score_font.render(f'{score_1} x {score_2}',
                                       True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)

    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()