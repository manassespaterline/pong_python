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
medium_font = pygame.font.SysFont('none', 28)
small_font = pygame.font.SysFont('none', 20)

start_game = False

player1_win = False
player2_win = False



bot_playing = False
friend_playing = False


def menu():

    global bot_playing
    global friend_playing

    global ball_vel_x
    global ball_vel_y

    global start_game

    ball_vel_x = 6
    ball_vel_y = 6

    start_game = False

    global bot_playing
    global friend_playing

    bot_playing = False
    friend_playing = False


    title = main_font.render("The Pong Game", True, 'white')

    txt_one_color = (255, 255, 255)
    txt_two_color = (255, 255, 255)
    txt_three_color = (255, 255, 255)
    txt_four_color = (255, 255, 255)

    

    play_bot_rect = pygame.Rect(screenWidth / 2 - 100, 220, 200, 50)
    play_local_rect = pygame.Rect(screenWidth / 2 - 100, 300, 200, 50)
    configuration_rect = pygame.Rect(screenWidth / 2 - 100, 380, 200, 50)
    exit_rect = pygame.Rect(screenWidth / 2 - 100, 460, 200, 50)

    blank_rect_one = pygame.Rect(screenWidth / 2 - 100, 220, 200, 50)
    blank_rect_two = pygame.Rect(screenWidth / 2 - 100, 300, 200, 50)
    blank_rect_three = pygame.Rect(screenWidth / 2 - 100, 380, 200, 50)
    blank_rect_four = pygame.Rect(screenWidth / 2 - 100, 460, 200, 50)

    running_menu = True
    while running_menu:

        screen.fill((48, 48, 48))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_bot_rect.collidepoint(mouse_pos):
                    bot_playing = True
                    running_menu = False
                if play_local_rect.collidepoint(mouse_pos):
                    friend_playing = True
                    running_menu = False
                if configuration_rect.collidepoint(mouse_pos):
                    print("config")
                if exit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(title, (screenWidth / 2 - 80, 100))

        pygame.draw.rect(screen, 'white', play_bot_rect, 2)
        pygame.draw.rect(screen, 'white', play_local_rect, 2)
        pygame.draw.rect(screen, 'white', configuration_rect, 2)
        pygame.draw.rect(screen, 'white', exit_rect, 2)

        play_bot_txt = medium_font.render("Play with bot", True, txt_one_color)
        play_local_txt = medium_font.render("Play with a friend", True, txt_two_color)
        config_txt = medium_font.render("Configurations", True, txt_three_color)
        exit_txt = medium_font.render("Exit", True, txt_four_color)


        screen.blit(play_bot_txt, (screenWidth / 2 - 80, 235))
        screen.blit(play_local_txt, (screenWidth / 2 - 80, 315))
        screen.blit(config_txt, (screenWidth / 2 - 80, 395))
        screen.blit(exit_txt, (screenWidth / 2 - 80, 475))


        if play_bot_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, 'white', blank_rect_one)
            txt_one_color = (0, 0, 0)
            screen.blit(play_bot_txt, (screenWidth / 2 - 80, 235))
        else:
            txt_one_color = (255, 255, 255)


        if play_local_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, 'white', blank_rect_two)
            txt_two_color = (0, 0, 0)
            screen.blit(play_local_txt, (screenWidth / 2 - 80, 315))
        else:
            txt_two_color = (255, 255, 255)



        if configuration_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, 'white', blank_rect_three)
            txt_three_color = (0, 0, 0)
            screen.blit(config_txt, (screenWidth / 2 - 80, 395))
        else:
            txt_three_color = (255, 255, 255)


        if exit_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, 'white', blank_rect_four)
            txt_four_color = (0, 0, 0)
            screen.blit(exit_txt, (screenWidth / 2 - 80, 475))
        else:
            txt_four_color= (255, 255, 255)


        credits = small_font.render("Made by Manassés. 2024. All rights reserved.", True, 'white')
        screen.blit(credits, (screenWidth / 2 - 140, 700))


        pygame.display.update()
        clock.tick(FPS)



def win():

    global player1_points
    global player1_win
    global player2_points
    global player2_win

    global bot_playing
    global friend_playing

    running_win = True
    while running_win:

        screen.fill((48, 48, 48))

        player1_points = 0
        player2_points = 0

        bot_playing = False
        friend_playing = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running_win = False
                    menu()

        if player1_win:
            p1_win_txt = main_font.render("PLAYER 1 WINS!", True, 'white')
            screen.blit(p1_win_txt, (screenWidth / 2 - 100, screenHeight / 2 - 30))
        if player2_win:
            p2_win_txt = main_font.render("PLAYER 2 WINS!", True, 'white')
            screen.blit(p2_win_txt, (screenWidth / 2 - 100, screenHeight / 2 - 30))


        play_again_txt = medium_font.render("Press ENTER to play again.", True, 'white')
        screen.blit(play_again_txt, (screenWidth / 2 - 130, 580))

        pygame.display.update()
        clock.tick(FPS)


menu()

running = True
while running:

    screen.fill((48, 48, 48))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    # PLAYER MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player_y -= player_vel
        start_game = True
    elif keys[K_s]:
        player_y += player_vel
        start_game = True
        

    # PLAYER DRAWING
    player_rect = pygame.Rect(player_x, player_y - (player_h / 2), player_w, player_h)
    pygame.draw.rect(screen, 'white', player_rect)

    # PLAYER BORDER LIMIT
    if player_rect.top <= 0:
        player_y = 0 + player_h / 2
    elif player_rect.bottom >= screenHeight:
        player_y = screenHeight - 50

    ball = ball.move(ball_vel)

    if start_game:
        ball_x += ball_vel[0]
        ball_y += ball_vel[1]

    if ball.top <= 0 or ball.bottom >= screenHeight:
        ball_vel[1] = -ball_vel[1]

    # BALL DRAWING
    ball = pygame.draw.circle(screen, 'white', (ball_x, ball_y), 8)

    if player_rect.colliderect(ball):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] += 1
        ball_vel[1] += 1


    # BOT DRAWING
    bot_rect = pygame.Rect(bot_x, bot_y - (bot_h / 2), bot_w, bot_h)
    pygame.draw.rect(screen, 'white', bot_rect)

    # BOT BORDER LIMIT
    if bot_rect.top <= 0:
        bot_y = 0 + bot_h / 2
    elif bot_rect.bottom >= screenHeight:
        bot_y = screenHeight - 50

    # BOT CONTROL P2
    if bot_playing:
        if bot_y > ball_y:
            bot_y -= bot_vel
        elif bot_y < ball_y:
            bot_y += bot_vel

    # FRIEND CONTROL P2
    if friend_playing:
        if keys[pygame.K_UP]:
            bot_y -= bot_vel
            start_game = True
        elif keys[pygame.K_DOWN]:
            bot_y += bot_vel
            start_game = True

    # P2 BALL COLLISION
    if bot_rect.colliderect(ball):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] -= 1
        ball_vel[1] -= 1


    #SEE WHO WINS!!!
    if ball.left < 0:
        player2_points += 1

        ball_vel_x = -6
        ball_vel_y = 6
        ball_vel = [ball_vel_x, ball_vel_y]

        ball_x = screenWidth / 2
        ball_y = screenHeight / 2

    if ball.right > screenWidth:
        player1_points += 1

        ball_vel_x = 6
        ball_vel_y = 6
        ball_vel = [ball_vel_x, ball_vel_y]

        ball_x = screenWidth / 2
        ball_y = screenHeight / 2
    
    # WRITE THE PONTUATION
    points = main_font.render(f"{player1_points} - {player2_points}", True, 'white')
    screen.blit(points, ((screenWidth / 2 - 20), 40))

    # WIN
    if player1_points == 5:
        player1_win = True
        win()
    if player2_points == 5:
        player2_win = True
        win()

    pygame.display.update()
    clock.tick(FPS)