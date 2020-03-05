import pygame
from sprites import block
from random import randint

HEIGHT = 700

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
colors = [red,green,blue]

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
def check_rect_collision(block,blocks):
    collision = -1
    collision = block.rect.collidelist(blocks)
    if collision != -1:
            if block.color == blocks[collision].color:
                return collision
            else:
                return exit()
    return -1
        

def menu_handler(playrect,exitrect,screen):
    mouse = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if playrect.collidepoint(mouse[0],mouse[1]):
            screen.fill((0,0,100))
            pygame.mouse.set_visible(False)
            return True
        elif exitrect.collidepoint(mouse[0],mouse[1]):
            print('exiting')
            exit()
    return False

def block_gen(listOfBlocks,speed):
    rand_color = colors[randint(0,2)]
    all_blocks_floored = True
    for b in listOfBlocks:
        if b.rect.y < HEIGHT - 40:
            all_blocks_floored = False
            #print("currently falling at y: ",listOfBlocks[len(listOfBlocks)-1].rect.y)

    if all_blocks_floored:
        speed +=1
        newBlock = block(40,40,rand_color)
        newBlock.speed = speed
        listOfBlocks.append(newBlock)
        #distribute_blocks(list_of_all_blocks,newBlock)
        
    return speed

def distribute_blocks(list_of_all_blocks,block):
    if block.color == red:
        list_of_all_blocks[0].append(block)
    if block.color == green:
        list_of_all_blocks[1].append(block)
    if block.color == blue:
        list_of_all_blocks[2].append(block)



def menu(screen):
    font = pygame.font.Font('freesansbold.ttf', 60)

    play = font.render('PLAY', True, (255,255,255), (255,0,0)) 

    playRect = play.get_rect() 
    playRect.center = (250,100)

    Exit = font.render('EXIT', True, (255,255,255), (255,0,0)) 

    ExitRect = Exit.get_rect() 
    ExitRect.center = (250,200)

    screen.blit(play,playRect)
    screen.blit(Exit,ExitRect)

    flag = menu_handler(playRect,ExitRect,screen)
    return flag

    

