import pygame
import os

# set height and width for the scaling of the background
WIDTH = 800
HEIGHT = WIDTH
#get absolute path to assets folder 
ABSOLUTE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets")

#load enemy ships
RED_ENEMY_SHIP = pygame.image.load(os.path.join(ABSOLUTE_PATH,"red_ship.png"))
BLUE_ENEMY_SHIP = pygame.image.load(os.path.join(ABSOLUTE_PATH,"blue_ship.png"))
GREEN_ENEMY_SHIP = pygame.image.load(os.path.join(ABSOLUTE_PATH,"green_ship.png"))

#load user ship
USER_SHIP = pygame.image.load(os.path.join(ABSOLUTE_PATH,"user_ship.png"))

#load lasers
BLUE_LASER = pygame.image.load(os.path.join(ABSOLUTE_PATH,"blue_laser.png"))
GREEN_LASER = pygame.image.load(os.path.join(ABSOLUTE_PATH,"green_laser.png"))
RED_LASER = pygame.image.load(os.path.join(ABSOLUTE_PATH,"red_laser.png"))
YELLOW_LASER = pygame.image.load(os.path.join(ABSOLUTE_PATH,"yellow_laser.png"))

#load background and scale to size
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(ABSOLUTE_PATH,"background-black.png")), (WIDTH,HEIGHT))