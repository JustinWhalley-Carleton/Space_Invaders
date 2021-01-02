import pygame
from colors import *

# display how to play text
def how_to_play(width):
    TEXTSPACING = 20
    HEADERSPACING = 25
    PARAGRAPHSPACING = 10

    display_surface = pygame.display.set_mode((width,width))

    pygame.display.set_caption('How To')

   
    header_font = pygame.font.Font('freesansbold.ttf', 20)
    text_font = pygame.font.SysFont('timesnewroman',15)
    
  
    header1 = make_header("Goal")
    text1 = make_text("Last as long as possible before dying. User has 100 health(can take 10 lasers or 10 collisions) before dying.")

    header2 = make_header("How to Play")
    text2 = make_text("Use the arrow keys to move and use the spacebar is shoot.")

    header3 = make_header("Levels")
    text3 = make_text("Every level adds 5 extra enemies.")

    header3 = make_header("Go Back To Menu")
    text3 = make_text("To go back to menu, push key 'c'")


    while True:
        display_surface.fill(WHITE)

        i = 0
        j = 0

        display_surface.blit(header1, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text1, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING

        display_surface.blit(header2, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text2, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING

        display_surface.blit(header3, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text3, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING
        
       
        for event in pygame.event.get():
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pygame.display.set_caption("Menu")
                    return
            
            if event.type == pygame.QUIT:
    
                pygame.quit()
    
                quit()
            pygame.display.update()
# make header text
def make_header(text):
    header_font = pygame.font.Font('freesansbold.ttf', 20)
    return header_font.render(text, True, BLACK, WHITE)
# make regular text
def make_text(text):
    text_font = pygame.font.SysFont('timesnewroman',15)
    return text_font.render(text, True, BLACK, WHITE)