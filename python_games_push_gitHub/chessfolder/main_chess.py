import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chessboard")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_chessboard():
    block_size = 100 # set the size of the grid block
    for x in range(0, 800, block_size):
        for y in range(0, 800, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            if (x + y) // block_size % 2 == 0:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_chessboard()
    pygame.display.flip()
