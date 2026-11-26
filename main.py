import pygame
import time
import random
import math
from Objects.Tower import Tower
from Objects.Enemy import Enemy
BG = (230, 230, 230)
WIDTH = 600
HEIGHT = 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# will need to test



def draw():
    WIN.fill(BG)
    tower = Tower(100, 1, 300, 300, 0)
    tower.draw(WIN)
    tower.draw_range_circle(WIN, 30)
    pygame.display.update()


def main():
    
    fps = 60
    clock = pygame.time.Clock()
    run = True

    while run:   
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()



if __name__ == "__main__":

    main()