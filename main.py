import pygame, sys
from pygame.locals import *

pygame.init()

screenSize = screenWidth, screenHeight = 1280, 720
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60

player_x = 80
player_y = 360
player_w = 20
player_h = 100
player_vel = 5

ball_x = screenWidth / 2
ball_y = screenHeight / 2


ball_vel_x = 6
ball_vel_y = 6
ball_vel = [ball_vel_x, ball_vel_y]


#BOT CONFIG
bot_x = 1200
bot_y = 360
bot_w = 20
bot_h = 100
bot_vel = 5

#ball draw
ball = pygame.draw.circle(screen, 'white', (ball_x, ball_y), 8)

#points
player1_points = 0
player2_points = 0

main_font = pygame.font.SysFont('none', 32)

start_game = False

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
        start_game = True
    elif keys[K_s]:
        player_y += player_vel
        start_game = True
    elif keys[K_UP]:
        player_y -= player_vel
        start_game = True
    elif keys[K_DOWN]:
        player_y += player_vel
        start_game = True
        

    #player draw
    player_rect = pygame.Rect(player_x, player_y - (player_h / 2), player_w, player_h)
    pygame.draw.rect(screen, 'white', player_rect)

    if player_rect.top <= 0:
        player_y = 0 + player_h / 2
    elif player_rect.bottom >= screenHeight:
        player_y = screenHeight - 50

    ball = ball.move(ball_vel)

    if start_game:
        ball_x += ball_vel[0]
        ball_y += ball_vel[1]
    '''if ball.left <= 0 or ball.right >= screenWidth:
        ball_vel[0] = -ball_vel[0]'''
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
        ball_vel[0] += 1
        ball_vel[1] += 1



    #BOT DRAWING
    bot_rect = pygame.Rect(bot_x, bot_y - (bot_h / 2), bot_w, bot_h)
    pygame.draw.rect(screen, 'white', bot_rect)

    if bot_y > ball_y:
        bot_y -= bot_vel
    elif bot_y < ball_y:
        bot_y += bot_vel
    if bot_rect.colliderect(ball):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] -= 1
        ball_vel[1] -= 1


    #SEE WHO WINS!!!
    if ball.left < 0:
        player2_points += 1

        player_x = 80
        player_y = 360

        bot_x = 1200
        bot_y = 360

        ball_vel_x = 6
        ball_vel_y = 6
        ball_vel = [ball_vel_x, ball_vel_y]

        ball_x = screenWidth / 2
        ball_y = screenHeight / 2
        start_game = False


    if ball.right > screenWidth:
        player1_points += 1

        player_x = 80
        player_y = 360

        bot_x = 1200
        bot_y = 360

        ball_vel_x = 6
        ball_vel_y = 6
        ball_vel = [ball_vel_x, ball_vel_y]

        ball_x = screenWidth / 2
        ball_y = screenHeight / 2
        start_game = False
    
    points = main_font.render(f"{player1_points} - {player2_points}", True, 'white')
    screen.blit(points, ((screenWidth / 2 - 20), 40))

    print(ball_vel)

    pygame.display.update()
    clock.tick(FPS)