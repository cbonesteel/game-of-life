import sys, pygame
import startPositions
from events import *
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
window_width = 1440
window_height = 820

rows = 82
cols = 144

currentGen = [[0] * cols for _ in range(rows)]
nextGen = [[0] * cols for _ in range(rows)]


def main():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    done = False
    paused = True
    tick = 10

    screen.fill(white)
    
    while not done:
        clock.tick(tick)
        
        if not paused:
            screen.fill(white)
            drawCurrentGen()
            findNextGen()
            updateCurrentGen()
        else:
            drawCurrentGen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    if paused:
                        pygame.event.post(pygame.event.Event(UNPAUSEGAME, {}))
                    else:
                        pygame.event.post(pygame.event.Event(PAUSEGAME, {}))
                if event.key == K_ESCAPE:
                    done = True
                if event.key == K_RIGHT:
                    tick += 1
                if event.key == K_LEFT:
                    if tick != 1:
                        tick -= 1
            
            if event.type == pygame.MOUSEBUTTONDOWN and paused:
                pressed = pygame.mouse.get_pressed()
                if pressed[0]:
                    x,y = pygame.mouse.get_pos()
                    x = int(x / 10)
                    y = int(y / 10)
                    currentGen[y][x] = 1
                elif pressed[2]:
                    x,y = pygame.mouse.get_pos()
                    x = int(x / 10)
                    y = int(y / 10)
                    currentGen[y][x] = 0

            if event.type == PAUSEGAME:
                paused = True
            if event.type == UNPAUSEGAME:
                paused = False
                
        pygame.display.update()

    pygame.quit()
    sys.exit()

def drawGrid():
    blockSize = 10 #Set the size of the grid block
    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, black, rect, 1)

def drawCurrentGen():
    blockSize = 10
    for x in range(0, window_height, blockSize):
        for y in range(0, window_width, blockSize):
            if currentGen[int(x/10)][int(y/10)] == 1:
                rect = pygame.Rect(y, x, blockSize, blockSize)
                pygame.draw.rect(screen, black, rect, 0)
            else:
                rect = pygame.Rect(y, x, blockSize, blockSize)
                pygame.draw.rect(screen, white, rect, 0)

def findNumAdjacent(row, col):
    counter = 0

    top = False
    bot = False
    left = False
    right = False
    
    if row - 1 < 0:
        top = True
    elif row + 1 >= rows:
        bot = True

    if col - 1 < 0:
        left = True
    elif col + 1 >= cols:
        right = True

    if not top and not bot and not left and not right:
        counter += currentGen[row-1][col-1] + currentGen[row-1][col] + currentGen[row-1][col+1]
        counter += currentGen[row][col-1] + currentGen[row][col+1]
        counter += currentGen[row+1][col-1] + currentGen[row+1][col] + currentGen[row+1][col+1]
    elif top:
        counter += currentGen[rows-1][col] + currentGen[row+1][col]
        if left:
            counter += currentGen[rows-1][cols-1] + currentGen[row][cols-1] + currentGen[row+1][cols-1]
            counter += currentGen[rows-1][col+1] + currentGen[row][col+1] + currentGen[row+1][col+1]
        elif right:
            counter += currentGen[rows-1][col-1] + currentGen[row][col-1] + currentGen[row+1][col-1]
            counter += currentGen[rows-1][0] + currentGen[row][0] + currentGen[row+1][0]
        else:
            counter += currentGen[rows-1][col-1] + currentGen[row][col-1] + currentGen[row+1][col-1]
            counter += currentGen[rows-1][col+1] + currentGen[row][col+1] + currentGen[row+1][col+1]
    elif bot:
        counter += currentGen[row-1][col] + currentGen[0][col]
        if left:
            counter += currentGen[row-1][cols-1] + currentGen[row][cols-1] + currentGen[0][cols-1]
            counter += currentGen[row-1][col+1] + currentGen[row][col+1] + currentGen[0][col+1]
        elif right:
            counter += currentGen[row-1][col-1] + currentGen[row][col-1] + currentGen[0][col-1]
            counter += currentGen[row-1][0] + currentGen[row][0] + currentGen[0][0]
        else:
            counter += currentGen[row-1][col-1] + currentGen[row][col-1] + currentGen[0][col-1]
            counter += currentGen[row-1][col+1] + currentGen[row][col+1] + currentGen[0][col+1]
    elif left:
        counter += currentGen[row-1][cols-1] + currentGen[row-1][col] + currentGen[row-1][col+1]
        counter += currentGen[row][cols-1] + currentGen[row][col+1]
        counter += currentGen[row+1][cols-1] + currentGen[row+1][col] + currentGen[row+1][col+1]
    elif right:
        counter += currentGen[row-1][col-1] + currentGen[row-1][col] + currentGen[row-1][0]
        counter += currentGen[row][col-1] + currentGen[row][0]
        counter += currentGen[row+1][col-1] + currentGen[row+1][col] + currentGen[row+1][0]

    return counter

def findNextGen():
    for i in range(rows):
        for j in range(cols):
            neighbors = findNumAdjacent(i, j)
            if currentGen[i][j] == 1:
                if neighbors < 2:
                    nextGen[i][j] = 0
                elif neighbors > 3:
                    nextGen[i][j] = 0
                else:
                    nextGen[i][j] = 1
            else:
                if neighbors == 3:
                    nextGen[i][j] = 1

def updateCurrentGen():
    for i in range(rows):
        for j in range(cols):
            currentGen[i][j] = nextGen[i][j]
            nextGen[i][j] = 0

if __name__ == '__main__':
    main()
