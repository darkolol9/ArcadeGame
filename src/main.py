import pygame
from event import event_handler
import sprites



pygame.init()

width,height = 700,700
screen = pygame.display.set_mode((width,height))
block = sprites.block(60,60)
#game loop
while True:
    screen.fill((0,0,0))

    #eventhandler goes here
    event_handler()
    block.update()
    block.blit(screen)
    #updates

    pygame.display.flip()