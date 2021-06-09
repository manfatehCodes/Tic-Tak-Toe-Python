import pygame, sys
import numpy as np

pygame.init()

WIDTH=600
HIGHT=600
LINE_WIDTH=15
BG_COLOR = (28, 170, 156)
RED=(255, 0, 0)
LINE_COLOR=(23, 145, 135)
BOARD_ROWS=3
BOARD_CLMS=3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOR=(239, 231, 200)
CROSS_WIDTH = 25
SPACE = 55
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)
board=np.zeros((BOARD_ROWS, BOARD_CLMS))

#pygame.draw.line(screen, RED, (10, 10), (300, 300), 10)

def line_maker():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

player = 1

def draw_fig():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_CLMS):
            if board [row] [col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, ( int(col * 200 + 200 / 2), int(row *200 + 200 / 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board [row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col *200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 -SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_CLMS):
            if board [row][col] == 0:
                return  False
    return True

def check_win(player):
    # verticle win check
    for col in range(BOARD_CLMS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            verticle_winning_line(col, player)
            return True
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontal_wining_line(row, player)
            return True
        # asc diagonal win check
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            asc_diagonal(player)
            return True

    # desc diagonal win chek
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        deasc_diagonal(player)
        return True

    return False

def verticle_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HIGHT - 15), LINE_WIDTH)

def horizontal_wining_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), LINE_WIDTH)

def asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, HIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)

def deasc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HIGHT - 15), LINE_WIDTH)


def restart():
    screen.fill(BG_COLOR)
    line_maker()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_CLMS):
            board[row][col] = 0


line_maker()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex = event.pos[0] #x axis
            mousey = event.pos[1] #y axis

            clicked_row = int(mousey // 200)
            clicked_col = int(mousex // 200)


            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    check_win(player)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    check_win(player)
                    player = 1

                draw_fig()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart()
    pygame.display.update()