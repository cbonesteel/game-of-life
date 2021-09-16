import sys, pygame
pygame.init()

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

    screen.fill(white)

    currentGen[5][5] = 1
    currentGen[5][6] = 1
    currentGen[6][6] = 1
    currentGen[6][5] = 1

    currentGen[5][15] = 1
    currentGen[6][15] = 1
    currentGen[7][15] = 1

    currentGen[4][16] = 1
    currentGen[8][16] = 1

    currentGen[3][17] = 1
    currentGen[9][17] = 1
    currentGen[3][18] = 1
    currentGen[9][18] = 1

    currentGen[6][19] = 1

    currentGen[4][20] = 1
    currentGen[8][20] = 1

    currentGen[5][21] = 1
    currentGen[6][21] = 1
    currentGen[7][21] = 1

    currentGen[6][22] = 1

    currentGen[3][25] = 1
    currentGen[4][25] = 1
    currentGen[5][25] = 1

    currentGen[3][26] = 1
    currentGen[4][26] = 1
    currentGen[5][26] = 1

    currentGen[2][27] = 1
    currentGen[6][27] = 1

    currentGen[1][29] = 1
    currentGen[2][29] = 1
    currentGen[6][29] = 1
    currentGen[7][29] = 1

    currentGen[3][39] = 1
    currentGen[3][40] = 1
    currentGen[4][40] = 1
    currentGen[4][39] = 1
    
    while not done:
        clock.tick(10)
        
        screen.fill(white)
        drawGrid()
        drawCurrentGen()
        findNextGen()
        updateCurrentGen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        pygame.display.update()

    pygame.quit()

    
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
                            
def findNumAdjacent(row, col):
    counter = 0

    rowUp = row - 1
    rowDown = row + 1
    colLeft = col - 1
    colRight = col + 1
    
    top = False
    bot = False
    left = False
    right = False
    
    # Checks for center cell
    if rowUp >= 0 and colLeft >= 0 and rowDown < rows - 1 and colRight < cols - 1:
        counter += currentGen[rowUp][colLeft] + currentGen[rowUp][col] + currentGen[rowUp][colRight]
        counter += currentGen[row][colLeft] + currentGen[row][colRight]
        counter += currentGen[rowDown][colLeft] + currentGen[rowDown][col] + currentGen[rowDown][colRight]
        return counter

    if rowUp < 0:
        top = True
        counter += currentGen[rows - 1][col]
        counter += currentGen[rowDown][col]
    elif rowDown > rows - 1:
        bot = True
        counter += currentGen[0][col]
        counter += currentGen[rowUp][col]
        
    if colLeft < 0:
        left = True
        counter += currentGen[row][cols - 1]
        counter += currentGen[row][colRight]
    elif colRight > cols - 1:
        right = True
        counter += currentGen[row][colLeft]
        counter += currentGen[row][0]

    if top and left:
        counter += currentGen[rows - 1][cols - 1] + currentGen[rows - 1][colRight]
        counter += currentGen[rowDown][cols - 1] + currentGen[rowDown][colRight]
    elif top and right:
        counter += currentGen[rows - 1][colLeft] + currentGen[rows - 1][0]
        counter += currentGen[rowDown][colLeft] + currentGen[rowDown][0]
    elif bot and left:
        counter += currentGen[rowUp][cols - 1] + currentGen[rowUp][colRight]
        counter += currentGen[0][cols - 1] + currentGen[0][colRight]
    elif bot and right:
        counter += currentGen[rowUp][colLeft] + currentGen[rowUp][0]
        counter += currentGen[rows - 1][colLeft] + currentGen[rows - 1][0]
    elif top:
        counter += currentGen[rows - 1][colLeft] + currentGen[rows - 1][colRight]
        counter += currentGen[rowDown][colLeft] + currentGen[rowDown][colRight]
    elif bot:
        counter += currentGen[rowUp][colLeft] + currentGen[rowUp][colRight]
        counter += currentGen[0][colLeft] + currentGen[0][colRight]
    elif left:
        counter += currentGen[rowUp][cols - 1] + currentGen[rowUp][colRight]
        counter += currentGen[rowDown][cols - 1] + currentGen[rowDown][colRight]
    elif right:
        counter += currentGen[rowUp][colLeft] + currentGen[rowUp][0]
        counter += currentGen[rowDown][colLeft] + currentGen[rowDown][0]
    
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


main()
