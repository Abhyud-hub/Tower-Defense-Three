import pygame
import time
import math
import Tower

class TestTower(Tower):
    def __init__(self, x, y, health, image, level, weapon_img):
        super.__init__(x, y, health, image, level)
        self.weapon_img = weapon_img


