import sys, pygame, time
from pygame.locals import *
import random

WHITE = (255,255,255)
BLACK = (0,0,0)
N = 18
HEIGHT = 30
WIDTH = 30
MARGIN = 2
WINDOW_SIZE = [580,580]

pygame.init()
DISPLAY = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Nokia Snake")

#build Sudoku board
DISPLAY.fill(WHITE)

#get board
Board = [[]]
for row in range(N):
    color = WHITE
    tmp = []
    for col in range(N):
        margin1 = ((MARGIN + WIDTH) * row + MARGIN)
        margin2 = ((MARGIN + HEIGHT) * col + MARGIN)
        pygame.draw.rect(DISPLAY,
                         BLACK,
                         [(MARGIN + WIDTH) * col + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])
        tmp.append((margin1,margin2))
    Board.append(tmp)

def random_apple():
    x,y = random.randint(0, N-1), random.randint(0, N-1)
    AAPL_color = (255,0,0)
    # print(x,y)
    color_square(x,y,AAPL_color)

snake_speed = 1
#snake_length = 1 # length of snake_pos
snake_pos = [(0,0)]
snake_color = (0,255,0)


def Snake():
    x,y = random.randint(1, N-1), random.randint(1, N-1)
    #head of snake
    snake_pos[0] = (x,y)
    color_square(x,y,snake_color)

def color_square(x,y,color):
    #convert to board coordinates
    # print(x,y,str(color))
    # margin1,margin2 = Board[x][y]
    margin1 = ((MARGIN + WIDTH) * x + MARGIN)
    margin2 = ((MARGIN + HEIGHT) * y + MARGIN)
    pygame.draw.rect(DISPLAY,color,[margin1,margin2,WIDTH,HEIGHT])

    pygame.display.flip()
    pygame.display.update()

def movement(dir):
    #delete prev snake
    for x,y in snake_pos:
        color_square(x,y,BLACK)
    #draw moved snake
    new_x, new_y = snake_pos[0][0],snake_pos[0][1]
    # print('new ',new_x,new_y)
    if dir == 'N':
        new_y= new_y - 1
    if dir == 'S':
        new_y= new_y + 1
    if dir == 'E':
        new_x= new_x + 1
    if dir == 'W':
        new_x= new_x - 1
    #tail moves
    snake_pos.pop()
    snake_pos.append((new_x,new_y))
    #to new position
    if new_x <= N-1 and new_y<= N-1:
        if new_x >= 0 and new_y >= 0:
            color_square(new_x,new_y,snake_color)
    else:
        # print("ELSE")
        pygame.quit()
        sys.exit()

#MAIN GAME LOOP
loop = True
Snake()
random_apple()
direction = ''
#start game
while loop:

    for event in pygame.event.get():

        if event.type == QUIT or not loop:
            pygame.quit()
            sys.exit()

        #game starts
        if event.type == pygame.KEYDOWN:
            #change direction
            if event.key == pygame.K_LEFT:
                direction = 'W'
            if event.key == pygame.K_RIGHT:
                direction = 'E'
            if event.key == pygame.K_UP:
                direction = 'N'
            if event.key == pygame.K_DOWN:
                direction = 'S'
        #non-stopping snake
        movement(direction)
        time.sleep(0.7)

        pygame.display.flip()
        pygame.display.update()
