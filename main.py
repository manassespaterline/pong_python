import pygame, sys
from pygame.locals import *

pygame.init()

screenSize = screenWidth, screenHeight = 1280, 720
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60

player_y = 360
player_w = 20
player_h = 100
player_vel = 8

ball_x = screenWidth / 2
ball_y = screenHeight / 2

ball_vel = [5, 5]

start_game = False

#ball draw
ball = pygame.draw.circle(screen, 'white', (ball_x, ball_y), 8)

running = True
while running:

    screen.fill((48, 48, 48))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #player movement
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player_y -= player_vel
    elif keys[K_s]:
        player_y += player_vel
    elif keys[K_UP]:
        player_y -= player_vel
    elif keys[K_DOWN]:
        player_y += player_vel
        

    #player draw
    player_rect = pygame.Rect(80, player_y - (player_h / 2), player_w, player_h)
    pygame.draw.rect(screen, 'white', player_rect)

    if player_rect.top <= 0:
        player_y = 0 + player_h / 2
    elif player_rect.bottom >= screenHeight:
        player_y = screenHeight - 50

    ball = ball.move(ball_vel)


    ball_x += ball_vel[0]
    ball_y += ball_vel[1]
    if ball.left <= 0 or ball.right >= screenWidth:
        ball_vel[0] = -ball_vel[0]
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ball_vel[1] = -ball_vel[1]

    '''if ball_x >= screenWidth:
        ball_x = screenWidth / 2
        ball_y = screenHeight / 2'''
    '''if ball_x <= 0:
        ball_x = screenWidth / 2
        ball_y = screenHeight / 2'''

    #ball draw
    ball = pygame.draw.circle(screen, 'white', (ball_x, ball_y), 8)

    if player_rect.colliderect(ball):
        ball_vel[0] = -ball_vel[0]

    print(ball_x, ball_y)

    pygame.display.update()
    clock.tick(FPS)