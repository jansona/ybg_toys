print("Please keep waiting, it may take some time...")


import sys
# import time
import pygame
from MinMaxAlgorithm import MinMaxAlgorithm, get_result
from ABPAlgorithm import ABPAlgorithm


options = ["人机对弈：y/n\n", "是否先手：y/n\n", "1.极小极大算法；2.alpha-beta剪枝算法：\n"]

with_ai = True
is_white = False
algorithm = 1

i = 0
while i < len(options):
    choice = input(options[i])

    if i == 0:
        if choice == 'y':
            with_ai = True
        elif choice == 'n':
            with_ai = False
            break
        else:
            print("无效选项: {}".format(choice))
            continue
    elif i == 1:
        if choice == 'y':
            is_white = True
        elif choice == 'n':
            is_white = False
        else:
            print("无效选项: {}".format(choice))
            continue
    elif i == 2:
        if choice == '1':
            algorithm = 1
        elif choice == '2':
            algorithm = 2
        else:
            print("无效选项: {}".format(choice))
            continue
    i += 1

pygame.init()

BOARD_SIZE = 480
size = width, height = BOARD_SIZE, BOARD_SIZE
color = (17, 1, 51)
BLACK = (0, 145, 142)
WHITE = (255, 220, 52)
LINE_COLOR = (77, 213, 153)
screen = pygame.display.set_mode(size)

GRID_WIDTH = int(BOARD_SIZE / 3)

board_condition = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

screen.fill(color)

for i in range(1, 3):
    pygame.draw.line(screen, LINE_COLOR, (GRID_WIDTH * i, 0), (GRID_WIDTH * i, BOARD_SIZE), 1)
    pygame.draw.line(screen, LINE_COLOR, (0, GRID_WIDTH * i), (BOARD_SIZE, GRID_WIDTH * i), 1)

def draw_piece():

    for y in range(3):
        for x in range(3):
            piece_con = board_condition[y][x]
            if piece_con != 0 :
                if piece_con == 1:
                    piece_color = WHITE
                elif piece_con == -1:
                    piece_color = BLACK
                pygame.draw.circle(screen, piece_color,
                    (int((x + 0.5) * GRID_WIDTH), int((y + 0.5) * GRID_WIDTH)), int(GRID_WIDTH / 2) - 10)

difficult = 10

ai_algorithm = None
if with_ai:
    ai_piece = None
    if is_white:
        ai_piece = -1
    else:
        ai_piece = 1

    if algorithm == 1:
        ai_algorithm = MinMaxAlgorithm(ai_piece, difficult)
    elif algorithm == 2:
        ai_algorithm = ABPAlgorithm(ai_piece, difficult)

if not is_white and with_ai:

    board_condition[1][1] = 1
    draw_piece()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid = (int(event.pos[0] / (GRID_WIDTH + .0)),
                int(event.pos[1] / (GRID_WIDTH + .0)))
            # print(grid)
            
            y, x = grid
            i, j = x, y

            if board_condition[i][j] == 0:
                if with_ai:
                    if is_white:
                        board_condition[i][j] = 1

                        # start = time.time()
                        val, action = ai_algorithm(board_condition)
                        # end = time.time()
                        # print("algorithm {} takes {} s".format(algorithm, end - start))

                        if action:
                            mi, mj = action
                            board_condition[mi][mj] = -1
                    else:
                        board_condition[i][j] = -1
                        val, action = ai_algorithm(board_condition)
                        if action:
                            mi, mj = action
                            board_condition[mi][mj] = 1
                else:
                    if is_white:
                        board_condition[i][j] = 1
                    else:
                        board_condition[i][j] = -1
                    is_white = not is_white

            draw_piece()

            result = get_result(board_condition)

            if result == 1:
                if with_ai:
                    if is_white:
                        win_str = "You're winner!"
                    else:
                        win_str = "AI's winner!"
                else:
                    win_str = "The first player's winner!"
                font = pygame.font.SysFont("Arial", 70)
                win_surf = font.render(win_str, 1, (242, 3, 36))
                screen.blit(win_surf, [screen.get_width() / 2 - win_surf.get_width() / 2, 100])
            elif result == -1:
                if with_ai:
                    if is_white:
                        win_str = "AI's winner!"
                    else:
                        win_str = "You're winner!"
                else:
                    win_str = "The second player's winner!"
                font = pygame.font.SysFont("Arial", 70)
                win_surf = font.render(win_str, 1, (242, 3, 36))
                screen.blit(win_surf, [screen.get_width() / 2 - win_surf.get_width() / 2, 100])
            elif result == 0:
                stalemate_str = "Stalemate!"
                font = pygame.font.SysFont("Arial", 70)
                stalemate_surf = font.render(stalemate_str, 1, (242, 3, 36))
                screen.blit(stalemate_surf, [screen.get_width() / 2 - stalemate_surf.get_width() / 2, 100])

        pygame.display.flip()

pygame.quit()

