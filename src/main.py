import pygame
from event import event_handler
from event import menu_handler
from event import menu
import sprites


pygame.init()
pygame.display.set_caption(' GAME WINDOW ')

width,height = 700,700
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
block = sprites.block(40,40)
menu_screen_is_over = False

#game loop
while True:

    screen.fill((0,0,100))
    #eventhandler goes here
    event_handler()

    if menu_screen_is_over:

        #updates

        block.update()
        block.blit(screen)
        clock.tick(60)
        
    else :
        menu_screen_is_over =  menu(screen)
        

    pygame.display.flip()