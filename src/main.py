import pygame
from event import event_handler
from event import menu_handler
from event import menu
from event import block_gen
from event import check_rect_collision
import sprites
import random


red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
colors = [red,green,blue]

pygame.init()
pygame.display.set_caption(' GAME WINDOW ')

width,height = 700,700
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
global_speed = 4
block = sprites.block(40,40,colors[random.randint(0,2)])
menu_screen_is_over = False
collision = -1

listOfBlocks = [block]

while True: #game loop

    screen.fill((0,0,100))     #background
    
    event_handler()   #func to handle all events

    if menu_screen_is_over:

        for b in listOfBlocks:  #update and blit all blocks in the game
            b.update()
            b.blit(screen)

        clock.tick(30)

        collision = check_rect_collision(listOfBlocks[len(listOfBlocks)-1],listOfBlocks[:-1])

        if collision != -1:  #if there is a collision
            listOfBlocks.remove(listOfBlocks[collision])
            listOfBlocks.remove(listOfBlocks[len(listOfBlocks)-1])

        global_speed = block_gen(listOfBlocks,global_speed)

    else :
        menu_screen_is_over =  menu(screen)

    pygame.display.flip()