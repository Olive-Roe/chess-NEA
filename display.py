import pygame
import sys
from pygame.locals import *
import gingerchess

pygame.init()

FPS_CLOCK = pygame.time.Clock()

width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption("Ginger Chess")


pieces = {"b": "chess_svgs/Chess_bdt45.svg"}

with open(pieces["b"], "r") as f:
    contents = f.read()


def display_board(board):
    square_size = 75
    startX = 0.5 * width - square_size * 4
    startY = 0.5 * height - square_size * 4
    X, Y = startX, startY
    # Draw grid
    for i in range(8):
        Y = startY
        for j in range(8):
            s = pygame.Surface((square_size, square_size))
            if (i + j) % 2 == 0:
                s.fill("white")
            else:
                s.fill("black")
            piece = board[i][j]
            if piece.upper() == piece:
                piece = piece.lower() + "l"
            else:
                piece = piece.lower() + "d"
            # imp = pygame.image.load(f"/Users/alan/Desktop/Wawa\ Documents/Personal/Coding\ Projects/gingerchess/chess_svgs/Chess_{piece}t45.svg").convert()
            imp = pygame.image.load(pieces["b"])
            # imp = pygame.transform.scale(imp, (square_size * 0.8, square_size * 0.8))
            screen.blit(s, (X, Y))
            screen.blit(
                imp,
                (X + square_size * 0.1, Y + square_size * 0.1),
            )
            # screen.blit(imp, (X + 40, Y + 40))
            Y += square_size
        X += square_size


screen.fill("grey")
display_board(gingerchess.a)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    FPS_CLOCK.tick(60)
