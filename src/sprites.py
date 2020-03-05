import pygame

HEIGHT = 700



class block:
    def __init__(self,h,w,color):
        self.img = pygame.Surface([h,w])
        self.img.fill(color)
        self.color = color
        self.rect = self.img.get_rect()
        self.rect.y = 0
        self.rect.x = 100
        self.speed = 3

    def update(self):
        self.pos = pygame.mouse.get_pos()
        if self.rect.y < HEIGHT- 40:
            self.rect.x = self.pos[0]
            self.rect.y += self.speed
        else:
            self.rect.y = HEIGHT -40
        
    
    def blit(self,screen):
        screen.blit(self.img,[self.rect.x,self.rect.y])
    


