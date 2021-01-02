import pygame
from loaded_images import *

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    # draw laser on window
    def draw(self,win):
        win.blit(self.img, (self.x,self.y))
    # move laser by vel
    def move(self,vel):
        self.y += vel
    # check if laser is off the screen
    def off_screen(self,height):
        return not(self.y <=height and self.y >=0)
    # check if the was a collision between the laser and object in parameter
    def collision(self,obj):
        return collide(obj,self)
# check if object 1 collided with object 2. Checked using masks so the hit box is the visable ship and not the square around it 
def collide(obj1,obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None