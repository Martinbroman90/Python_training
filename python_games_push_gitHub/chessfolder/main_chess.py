import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chessboard")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
def load_images():
    pieces = ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']
    colors = ['white', 'black']
    images = {}
    for color in colors:
        for piece in pieces:
            images[f'{color}_{piece}'] = pygame.image.load(f'images/{color}_{piece}.png')
    return images

# Draw the chessboard
def draw_chessboard():
    block_size = 100  # Set the size of the grid block
    for x in range(0, 800, block_size):
        for y in range(0, 800, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            if (x + y) // block_size % 2 == 0:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

# Place pieces on the board
def place_pieces(screen, images, board):
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if piece:
                screen.blit(images[piece], (x * 100, y * 100))

# Initialize the board
def initialize_board():
    return [
        ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
        ['black_pawn'] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        ['white_pawn'] * 8,
        ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
    ]

# Main loop
running = True
images = load_images()
board = initialize_board()
selected_piece = None
selected_pos = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x //= 100
            y //= 100
            if selected_piece:
                board[y][x] = selected_piece
                board[selected_pos[1]][selected_pos[0]] = None
                selected_piece = None
                selected_pos = None
            else:
                selected_piece = board[y][x]
                selected_pos = (x, y)

    draw_chessboard()
    place_pieces(screen, images, board)
    pygame.display.flip()