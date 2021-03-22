import sys, pygame, time
import random

WHITE = (255,255,255)
BLACK = (0,0,0)
APPLE_color = (255,0,0)
SNAKE_color = (0,255,0)

N = 18
HEIGHT = 30
WIDTH = 30
MARGIN = 2

WINDOW_SIZE = [580,580]

pygame.init()
DISPLAY = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Nokia Snake")

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def list_form(self):
        return [self.x,self.y]
    def val_x(self):
        return int(self.x)
    def val_y(self):
        return int(self.y)

#build Snake board
DISPLAY.fill(WHITE)

#get board
for row in range(N):
    color = WHITE
    for col in range(N):
        margin1 = ((MARGIN + WIDTH) * row + MARGIN)
        margin2 = ((MARGIN + HEIGHT) * col + MARGIN)
        pygame.draw.rect(DISPLAY,
                         BLACK,
                         [(MARGIN + WIDTH) * col + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

def random_draw(color):
    #generate random apple on map
    x,y = random.randint(0, N-1), random.randint(0, N-1)
    #update global apple location value
    pos = Point(x,y)
    #draw rectangle
    color_square(x,y,color)
    #return random pos coordinates
    return pos

def color_square(x,y,color):
    #convert to board coordinates
    margin1 = ((MARGIN + WIDTH) * x + MARGIN)
    margin2 = ((MARGIN + HEIGHT) * y + MARGIN)
    #draw rextangle on mapped coordinates
    pygame.draw.rect(DISPLAY,color,[margin1,margin2,WIDTH,HEIGHT])

def movement(dir):
    global apple_pos

    new_pos_x = snake_pos[0].val_x()
    new_pos_y = snake_pos[0].val_y()
    #delete prev snake
    color_square(new_pos_x,new_pos_y,BLACK)
    print("Blacking: ",snake_pos[0].list_form())
    #augment coordinates based on snake's direction
    if dir == 'N':
        new_pos_y = new_pos_y - 1
    if dir == 'S':
        new_pos_y = new_pos_y + 1
    if dir == 'E':
        new_pos_x = new_pos_x + 1
    if dir == 'W':
        new_pos_x = new_pos_x - 1

    #eating apple phase

    #no hit
    if snake_pos[0].list_form() != apple_pos.list_form():
        blk = snake_pos[len(snake_pos)-1]
        color_square(blk.val_x(),blk.val_y(),BLACK)
        snake_pos.pop()
    #hit
    else:
        print("hit")
        #new apple location
        apple_pos = random_draw(APPLE_color)

    #tail moves
    snake_pos.insert(0,(Point(new_pos_x,new_pos_y)))
    #to new position
    if new_pos_x <= N-1 and new_pos_y<= N-1:
        if new_pos_x >= 0 and new_pos_y >= 0:
            for bod in snake_pos:
                # color_square(new_pos_x,new_pos_y,SNAKE_color)
                color_square(bod.val_x(),bod.val_y(),SNAKE_color)

    else:
        pygame.quit()
        sys.exit()
    tmp = ''
    for i in range(0,len(snake_pos)):
        tmp += str(snake_pos[i].list_form())
    print(tmp)

#start game variables
loop = True
#Apple object location
# apple_pos = Point(0,0)
apple_pos = random_draw(APPLE_color)
# print(apple_pos)

#Snake body location
snake_pos = []
snake_pos.append(random_draw(SNAKE_color))

direction = ''

#MAIN GAME LOOP
while loop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT or not loop:
            pygame.quit()
            sys.exit()

        #game starts
        if event.type == pygame.KEYDOWN:
            #change direction
            if event.key == pygame.K_LEFT:
                direction = 'W'
            elif event.key == pygame.K_RIGHT:
                direction = 'E'
            elif event.key == pygame.K_UP:
                direction = 'N'
            elif event.key == pygame.K_DOWN:
                direction = 'S'
    #non-stopping snake
    movement(direction)

    pygame.display.flip()
    pygame.display.update()

    time.sleep(0.4)
