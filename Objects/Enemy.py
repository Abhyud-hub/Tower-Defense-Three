from utiles import blit_rotate_center
import math


class Enemy:
    def __init__(self, type, image, health, x, y):
        self.health = health
        self.image = image
        self.type = type
        self.heading = 0
        self.x = x
        self.y =y


    def turn_to(self, obj):# same
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
    
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.x -= horizontal
        self.y -= vertical

    def draw(self, win):
        blit_rotate_center(win, self.image, (self.x, self.y), self.heading)
        

    

        

