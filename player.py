from ship import *
from colors import *
from loaded_images import *
import pygame

class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img = USER_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
    #move player lasers up by vel and check for collision
    def move_lasers(self,vel,objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif not laser in self.lasers:
                continue
            else:
                for obj in objs:
                    if laser.collision(obj):
                        try:
                            self.lasers.remove(laser)
                        except:
                            continue
                        objs.remove(obj)
                        
    #draw player on window
    def draw(self,win):
        super().draw(win)
        self.healthBar(win)
    # create healthbar
    def healthBar(self,win):
        pygame.draw.rect(win, RED,(self.x,self.y+self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(win, GREEN,(self.x,self.y+self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))