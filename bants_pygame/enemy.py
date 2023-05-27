import pygame
import random

class Enemy():
    def __init__(self):
        self.x = 50
        self.y = 50
       # self.screen_w = w
       # self.screen_h = h
        player_w, player_h = 50, 50
        self.rect = pygame.rect.Rect(30, 30, player_w, player_h)
        self.numEnemies = 4
        self.Locations =[]
        self.img = "CITY_RAT.xcf"

    def makeEnemies(self):
        for enemy in range(self.numEnemies):
            xx = random.randint(100, 1100)
            yy = random.randint(100, 620)
            self.Locations.append([xx, yy, 50, 50])
    
    def spawnEnemy(self):
        xx = random.randint(100, 1100)
        yy = random.randint(100, 620)
        self.Locations.append([xx, yy, 50, 50])
    
    def putEnemies(self, screen):
        img_surface = pygame.image.load(self.img).convert_alpha()
        for enemy in range(self.numEnemies):
            screen.blit(img_surface, self.Locations[enemy])
    
    def moveEnemies(self):
        for enemy in range(self.numEnemies):   
            #list = [x[enemy] for x in self.Locations]      
            list = self.Locations[enemy]       
            #x or y
            numero = random.randint(0, 1)
            #direction
            numerodos = random.randint(0, 1)
            if numero == 0:
                if numerodos ==0:
                    list[0] += 3
                else: 
                    list[0] -= 3
            else:
                if numerodos == 0:
                    list[1] += 3
                else:
                    list[1] -= 3

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > 1280:
                self.rect.right = 1280
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > 720:
                self.rect.bottom = 720            

    def kill(self, playerRect):
        for enemy in self.numEnemies:
            if playerRect.x + 50 == self.Locations[enemy][0] and playerRect.y + 50 == self.Locations[enemy][1]:
                self.Locations.remove(enemy)
        self.spawnEnemy()
        return
        
    def isOver(self, screen):
        if self.numEnemies == 0:
            text_surface = self.font.render("YOU WIN", True, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (1280/2, 720/2)
            self.screen.blit(text_surface, text_rect)

    
