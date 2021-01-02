import pygame
import time
import random
from functools import partial
import pygame_menu
from colors import *
from enemy import *
from player import *
from how_to_play import *
#define GUI size
WIDTH,HEIGHT = 800,800
#set up window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")
#main function
def main():
    # initialize variables
    run = True
    FPS = 60
    level = 0
    lives = 5
    font = pygame.font.Font('freesansbold.ttf', 20)
    player_velocity = 5
    enemies = []
    wave_length = 5
    enemy_vel = 1
    player = Player(300,630)
    lost = False
    lost_count = 0
    clock = pygame.time.Clock()
    laser_vel = 6
    # redraw window function (made local to main to access the variables without making them parameters or global)
    def redraw_window():
        #draw background
        WIN.blit(BACKGROUND,(0,0))
        #add lives and level counters at top of the screen
        lives_label = font.render(f"Lives: {lives}", 1,(WHITE))
        level_label = font.render(f"Level: {level}",1,WHITE)
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH-level_label.get_width()-10,10))
        #draw all enemies on the window
        for enemy in enemies:
            enemy.draw(WIN)
        # draw the player on the window
        player.draw(WIN)
        #react to game lost
        if(lost):
            lost_label = font.render("GAME OVER",1,WHITE)
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2,HEIGHT/2))
        #update the window with changes
        pygame.display.update()
    #game loop
    while run:
        #set frames per second
        clock.tick(FPS)
        #draw the windwo
        redraw_window()
        #check if game was lost
        if lives < 0 or player.health <= 0:
            lost = True
            lost_count += 1
        #react to lost game
        if lost:
            #counter over, return to menu
            if lost_count > FPS *5:
                run = False
                break
            else:
                #increment counter
                lost_count+=1
                continue
        # if all enemies gone proceed to next level
        if len(enemies) == 0:
            #increment level and add 5 extra enemies
            level+=1
            wave_length +=5
            #create all enemies for the wave
            for i in range(wave_length):
                enemy = Enemy(random.randint(50,WIDTH-100), random.randint(-500*level/2,-100),random.choice(["red","blue","green"]))
                enemies.append(enemy)
        #react to keypresses and quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_velocity >=0:
            player.x-=player_velocity
        if keys[pygame.K_RIGHT] and player.x + player_velocity +player.get_width()<= WIDTH:
            player.x +=player_velocity
        if keys[pygame.K_UP] and player.y - player_velocity >=0:
            player.y-=player_velocity
        if keys[pygame.K_DOWN] and player.y+player_velocity+player.get_height()+20<=HEIGHT:
            player.y+=player_velocity
        if keys[pygame.K_SPACE]:
            player.shoot()
        #move enemies and enemy lasers down by enemy_vel and laser_vel respectively
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel,player)
            # 10% chance of each enemy shooting every frame
            if random.randint(0,10*FPS) == 1: 
                enemy.shoot()
            #check if player ship hit an enemy ship and if collision occured subtract 10 health from player and remove enemy
            if collide(enemy,player):
                player.health -= 10
                enemies.remove(enemy)
            # react to enemy getting to bottom of the screen
            if enemy.y +enemy.get_height() > HEIGHT:
                lives-=1
                enemies.remove(enemy)
        #move player lasers up by laser_vel
        player.move_lasers(-laser_vel,enemies)
    #display play again menu once game is over
    play_again_menu()

#display play again menu
def play_again_menu():
    pygame.display.set_caption("Menu")
    surface = pygame.display.set_mode((WIDTH,WIDTH))
    menu = pygame_menu.Menu(300,400,"Game Over",theme=pygame_menu.themes.THEME_BLUE)
    menu.add_button("Play Again",main)
    menu.add_button("How To Play", how_to_play)
    menu.add_button("Quit",pygame_menu.events.EXIT)
    menu.mainloop(surface)

#display main menu
def main_menu(): 
    pygame.init()
    pygame.display.set_caption("Menu")
    surface = pygame.display.set_mode((WIDTH,WIDTH))
    menu = pygame_menu.Menu(300,400,"Welcome",theme=pygame_menu.themes.THEME_BLUE)
    menu.add_button("Play",main)
    menu.add_button("How To Play", partial(how_to_play,WIDTH))
    menu.add_button("Quit",pygame_menu.events.EXIT)
    menu.mainloop(surface)

if __name__=="__main__":
    main_menu()