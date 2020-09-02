import pygame
from pygame.locals import *
import random
from Tablero import tablero


canvas = pygame.display.set_mode((1000, 1000))
pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

Sudoku = tablero(100)


def main():
    Sudoku.draw(canvas,myfont)


running = True

while running:
    canvas.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Sudoku.solve_sudoku()
    main()
    pygame.display.flip()

pygame.quit()
