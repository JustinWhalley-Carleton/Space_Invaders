from colors import *
from ship import *
from loaded_images import *
from laser import *

class Enemy(Ship):
    # dictionary to choose the ship and laser based on the key
    COLOR_DICT = {"red": (RED_ENEMY_SHIP,RED_LASER), "green": (GREEN_ENEMY_SHIP,GREEN_LASER), "blue": (BLUE_ENEMY_SHIP,BLUE_LASER)}
    def __init__(self,x,y,color,health=100):
        super().__init__(x,y,health)
        self.ship_img, self.laser_img = self.COLOR_DICT[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    #move down by vel
    def move(self,vel):
        self.y+=vel
    # shoot a laser from the enemy ship
    def shoot(self):
        if self.cool_down ==0:
            laser = Laser(self.x-10,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down = 1