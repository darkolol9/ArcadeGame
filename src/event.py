import pygame

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def menu_handler(playrect,exitrect,screen):
    mouse = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if playrect.collidepoint(mouse[0],mouse[1]):
            screen.fill((0,0,100))
            return True
        elif exitrect.collidepoint(mouse[0],mouse[1]):
            print('exiting')
            exit()
    return False


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

    

