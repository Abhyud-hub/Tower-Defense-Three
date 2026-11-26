import math
import pygame
import random
from utiles import pixel_collision, blit_text_center, blit_rotate_center, blit_text_center, WHITE


class Tower:


    def __init__(self, health, image, level, x, y):
        self.health = health
        self.level = level
        self.x = x
        self.y = y
        self.heading = 0
        self.image = image
        self.rangecircle = None

    def circle_collision(self, obj):
        pixel_collision(self, obj)

    def draw(self, win):
        blit_rotate_center(win, self.image, (self.x, self.y), self.heading)

    def turn_to(self, object):
        target_x, target_y = obj.x, obj.y#still pending
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radiant_angle = math.pi / 2 
        else:
            desired_radiant_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radiant_angle += math.pi

        angle_difference = self.angle - math.degrees(desired_radiant_angle)
        if angle_difference >= 180:
            angle_difference -= 360

        if angle_difference > 0:
            self.angle -= min(self.rotation_vel, abs(angle_difference))
        else:
            self.angle += min(self.rotation_vel, abs(angle_difference))        

    def upgrade_status(self):
        self.level += 1

    def range_circle(self, win, radius):
        self.rangecircle = pygame.draw.circle(win, WHITE, (self.x, self.y), radius)

#will probaby add more for when selected on side bar what will it do
# will have one function to detect if that happened or not, another to see what to do with that info
#maybe make a whole other class just for the sidebar
    

    