import pygame


class block:
    def __init__(self,h,w):
        self.img = pygame.Surface([h,w])
        self.img.fill((255,0,0))
        self.rect = self.img.get_rect()
        self.rect.y = 0
        self.rect.x = 100

    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.rect.x = self.pos[0]
        if self.rect.y > 700:
            self.rect.y = 0
        self.rect.y +=1
        

    def blit(self,screen):
        screen.blit(self.img,[self.rect.x,self.rect.y])
    


