import pygame
import random
import math

class Enemy():
    def __init__(self):
        self.x = 50
        self.y = 50
       # self.screen_w = w
       # self.screen_h = h
        player_w, player_h = 50, 50
        self.rect = pygame.rect.Rect(30, 30, player_w, player_h)
        self.numEnemies = 0
        self.Locations =[]
        self.enemyRects = []
        self.img = "CITY_RAT.xcf"
        self.distance = 0
        self.speed = 1.5
        self.enemySpawnTimes = []

    def makeEnemies(self, num):
        for enemy in range(num):
            xx = random.randint(100, 1100)
            yy = random.randint(100, 620)
            self.enemyRects.append(pygame.rect.Rect(xx, yy, 50, 50))
            self.Locations.append([xx, yy, 50, 50])
            self.numEnemies +=1

    
    def randomSpawnEnemies(self):
#FIXME rat spawn location not to spawn on person
#FIXME screen slows down a lot
        if len(self.enemySpawnTimes) != 0:
            for x in range(len(self.enemySpawnTimes)):
                currentTime = math.floor((pygame.time.get_ticks() - self.enemySpawnTimes[x])/1000)
                if currentTime > 10:
                    xx = 1200
                    yy = random.randint(100, 620)
                    self.enemyRects.append(pygame.rect.Rect(xx, yy, 50, 50))
                    self.Locations.append([xx, yy, 50, 50])
                    self.numEnemies +=1
                    self.enemySpawnTimes.pop(x)
    

    def putEnemies(self, screen):
        img_surface = pygame.image.load(self.img).convert_alpha()
        for enemy in range(self.numEnemies):
            screen.blit(img_surface, self.enemyRects[enemy])
    
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

    def movenum2(self, player):
        playerRect = player.getRect()
        xx = playerRect.left
        yy = playerRect.top
        for x in range(len(self.enemyRects)):
            radians = math.atan2(yy - self.enemyRects[x].left, xx - self.enemyRects[x].top)
            self.distance = int(math.hypot(xx - self.enemyRects[x].left, yy - self.enemyRects[x].top))

            dx = math.cos(radians) * 3
            dy = math.sin(radians) * 3

            if self.distance:
                self.distance -= 1
                if not(self.enemyRects[x].left < 50 or self.enemyRects[x].left > 1230):
                    self.enemyRects[x].left += dx
                if not(self.enemyRects[x].top < 50 or self.enemyRects[x].top > 670):
                    self.enemyRects[x].top += dy

        
    def isOver(self, screen):
        if self.numEnemies == 0:
            text_surface = self.font.render("YOU WIN", True, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (1280/2, 720/2)
            self.screen.blit(text_surface, text_rect)

    def move_towards_player(self, player, num):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player.getRect().left - self.enemyRects[num].x, player.getRect().top - self.enemyRects[num].y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.enemyRects[num].x += dx * self.speed
        self.enemyRects[num].y += dy * self.speed

