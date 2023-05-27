import random
import pygame
from rect import Shape


class NPC():


    def __init__(self, x, y, w, h, img, screen, voice):
        self.rect = pygame.Rect(x, y, w, h)
        self.npc_x, self.npc_y, self.npc_w, self.npc_h = x, y, w, h
        self.img = img
        self.screen = screen
        #voicelines
        self.voicelines = voice
        self.font = pygame.font.SysFont(None, 30)
        self.BLACK = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.right = False
        self.left = False

        self.speed_x = 5
        self.speed_y = 4
        self.xdirectional = 1    
        self.ydirectional = 1  
        


    def draw(self):
        img_surface = pygame.image.load(self.img).convert_alpha()
        Shape.drawRect(Shape, self.screen, self.npc_x-100, self.npc_y-75, 200, 50, (255,255,255))   
        self.screen.blit(img_surface, self.rect)
    
    
    #npc movement
    #def move(self):
    #random.randint(20 )

    def talk(self):
        #Shape.drawRect(Shape, self.screen, self.npc_x, self.npc_y + 20, 100, 50, (175,175,175))
        text_surface = self.font.render(self.voicelines, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.npc_x, self.npc_y-50)
        self.screen.blit(text_surface, text_rect)


    def move(self):

        self.clock.tick(60)  
        

        #check x left
        if self.rect.left <= 0 + self.npc_w:
            self.xdirectional *= -1
            self.speed_x = abs(self.speed_x) * self.xdirectional
        #check x right
        if self.rect.right >= 1280 - self.npc_w:
            self.xdirectional *= -1
            self.speed_x = abs(self.speed_x) * self.xdirectional
        #check y top
        if self.rect.top <= 0 + self.npc_h:
            self.ydirectional *= -1
            self.speed_y = abs(self.speed_y) * self.ydirectional
        #check y bot
        if self.rect.bottom >= 720 - self.npc_h:
            self.ydirectional *= -1
            self.speed_y = abs(self.speed_y) * self.ydirectional

        self.rect.left += self.speed_x
        self.rect.top += self.speed_y
        self.npc_x += self.speed_x
        self.npc_y += self.speed_y
    def checkCollision(self, player):
        pass

        
        

        #self.collide = pygame.Rect.colliderect(self, self.rect)
        #if self.collide:
        #    self.directional *= -1;    
