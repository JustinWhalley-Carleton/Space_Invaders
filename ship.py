from colors import *
from laser import * 
from loaded_images import *


class Ship:
    COOLDOWN = 20
    def __init__(self, x, y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down = 0
    #draw ship on window
    def draw(self,win):
        win.blit(self.ship_img, (self.x,self.y))
        for laser in self.lasers:
            laser.draw(win)
    #move lasers by vel and check for collision
    def move_lasers(self,vel,obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
    #cooldown for shooting
    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1
    #shoot laser
    def shoot(self):
        if self.cool_down ==0:
            laser = Laser(self.x,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down = 1
    #get width of ship
    def get_width(self):
        return self.ship_img.get_width()
    #get height of ship
    def get_height(self):
        return self.ship_img.get_height()