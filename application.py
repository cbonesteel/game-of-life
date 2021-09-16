import sys, pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
window_width = 960
window_height = 540

def main():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    screen.fill(white)
    
    while True:
        screen.fill(white)
        drawGrid()
        # drawGeneration()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def drawGrid():
    blockSize = 10 #Set the size of the grid block
    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, black, rect, 1)

main()
