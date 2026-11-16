import pygame
import time
import random
import math

WIDTH = 600
HEIGHT = 600



def draw():
    pass

def main():
    
    fps = 180
    clock = pygame.time.clock()

    while run:    
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False