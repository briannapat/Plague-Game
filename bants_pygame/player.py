import pygame
from rect import Shape

class Player:

    def __init__(self):
        self.x = 50
        self.y = 250
       # self.screen_w = w
       # self.screen_h = h
        player_w, player_h = 100, 100
        self.rect = pygame.rect.Rect(30, 30, player_w, player_h)
        self.inventory = []
        self.img = "BACKGROUND_CITY.xcf"
        self.coinimg = "COIN.xcf"
        self.health = 5
        self.gold = 100
        self.font = pygame.font.SysFont(None, 30)
        self.BLACK = (0,0,0)
        self.turned = False
        self.font = pygame.font.SysFont(None, 30)



    def getX(self):
        return self.x

    def getY(self):
        return self.y


    def draw(self, screen, img):    
        #pygame.draw.rect(screen, (0, 0, 255), self.rect)
        if self.turned:
            img_surface = pygame.image.load("doctor2.xcf").convert_alpha()
        else:
            img_surface = pygame.image.load(img).convert_alpha()
        screen.blit(img_surface, self.rect)

    def resetLocation(self, x, value):
        if value:
            self.rect.left = x
        else:
            self.rect.right = x


    def moveFarm(self, key, screen_w, screen_h):   
        if key[pygame.K_UP]:
            self.rect.move_ip(0, -2)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, 2)
        if key[pygame.K_LEFT]:
            self.turned = False
            self.rect.move_ip(-2, 0)        
        if key[pygame.K_RIGHT]:
            self.turned = True   
            self.rect.move_ip(2, 0)
   
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_w:
            self.rect.right = screen_w
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_h:
            self.rect.bottom = screen_h     

    def moveMain(self, key, screen_w, screen_h, xlocations):   
        if key[pygame.K_UP]:
            if not(self.rect.top < 105 and self.rect.right > 680 and self.rect.left < 1140):
                self.rect.move_ip(0, -2)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, 2)
        if key[pygame.K_LEFT]:
            self.turned = False
            if not(self.rect.top <=100 and (self.rect.right > 670 and self.rect.left < 1155)):
                self.rect.move_ip(-2, 0)
            else:
                #if abs(self.rect.left - 1155) < abs(self.rect.right - 670):
                if self.rect.left - 1155 > 670:
                    self.rect.left = 1160     
 
        if key[pygame.K_RIGHT]:
            self.turned = True 
            if not(self.rect.top <=100 and (self.rect.right > 670 and self.rect.left < 1155)):
                self.rect.move_ip(2, 0)
            else:
                #if abs(self.rect.left - 1155) > abs(self.rect.right - 670):
                if 1155 - self.rect.right < 670:
                    self.rect.right = 665 
   
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_w:
            self.rect.right = screen_w
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_h:
            self.rect.bottom = screen_h     

        #for MARKET BOUNDARY
      #  if self.rect.top > 100: 
            #inside
       #     if self.rect.left < 1155 and self.rect.right > 670:
         #       self.rect.top = 100  
        ##if self.rect.top <= 100 and (self.rect.left > 670 or self.rect.left < 1155):
            #if abs(self.rect.left - 670) > abs(self.rect.left - 1155):
                #self.rect.left = 670
            #else:
                #self.rect.left = 1155
            #outside

         #for NPC BOUNDARY  
        if self.rect.bottom > 520 and self.rect.bottom < 720:
            for x in xlocations:
                if self.rect.right > x and self.rect.right < x + 5:
                    self.rect.right = x
                if self.rect.left < x + 100 and self.rect.left > x + 95:
                    self.rect.left = x + 100
                if self.rect.right > x + 2 and self.rect.left < x + 98:    
                    if self.rect.bottom > 520 and self.rect.bottom < 600:
                        self.rect.bottom = 520
                    if self.rect.top < 610 and self.rect.top > 600:
                        self.rect.top = 610
                        
                   
               



             
 

             
       # if self.rect.top < 100:
       #     self.rect.top = 100 

        #for NPC Boundary
              
  


    #method for items and display items. pref hit tab to showinventory()
    def showInventory(self, screen):
        #makes a transparent surface
        #surface = pygame.Surface([1280,720], pygame.SRCALPHA, 32)
        #surface.convert_alpha()
        img_surface = pygame.image.load(self.img).convert_alpha()

        #screen.blit(pygame.transform.scale(img_surface, (100, 50)), self.rect1)
        #screen.blit(pygame.transform.scale(img_surface, (100, 50)), self.rect2)
        #screen.blit(pygame.transform.scale(img_surface, (100, 50)), self.rect3)




        #pygame.draw.rect(screen, (200,200,200), self.rect)
        #screen.blit(img_surface, self.rect1)
        #screen.blit(img_surface, self.rect2)
        #screen.blit(img_surface, self.rect3)

        text_surface1 = self.font.render(str(10), True, self.BLACK)
        text_surface2 = self.font.render(str(self.gold), True, self.BLACK)
        text_surface3 = self.font.render(str(self.health), True, self.BLACK)
#text_rect = text_surface.get_rect()
        #text_rect.center = (self.npc_x, self.npc_y-50)
        screen.blit(text_surface1, self.rect1)
        screen.blit(text_surface2, self.rect2)
        screen.blit(text_surface3, self.rect3)


    
    #helf bar
    def displayHealthGold(self, screen):
        Shape.drawRect(Shape, screen, 0, 720-20, 250, 20, (0,0,0))
        length = 0
        for x in range(self.health):
            Shape.drawRect(Shape, screen, length, 720-20, 45, 20, (0,250,0))
            length += 50
        Shape.drawRect(Shape, screen, 720-100, 1280 - 100, 100, 100, (175,175,175))
        img_surface = pygame.image.load(self.coinimg).convert_alpha()
        screen.blit(img_surface, (1280-100, 720-100))
        text_surface = self.font.render(str(self.gold), True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (1280-120, 670)
        screen.blit(text_surface, text_rect)

    def loseHealth(self):
        self.health = self.health-1

    def addHealth(self):
        self.health += 1

    def decreaseGold(self, amount):
        self.gold -= amount
    
    def increaseGold(self, amount):
        self.gold += amount

    #enemy class is abstract; rats bear
    #shopkeeper; put image transaparent; set items with images; set "are you sure" box
    #plague docta; collect ingredients/ medicine
    #go to table; turn in ingredients>medicine
    #background changes
    #timer and progress bar for plant growth
    #random timed voicelines
    #medicine on self or npc

    def moveWithCollides(self, key, screen_w, screen_h, rect):    
        #if abs(self.rect.top - rect.top) <=50 and abs(self.rect.left - rect.left) <=50:
        if key[pygame.K_UP]:
            self.rect.move_ip(0, -2)
            #print("up")
            if self.rect.colliderect(rect):
                self.rect.top = rect.bottom
            #if pygame.Rect.collidedict(playerDict, rect):
                self.rect.move_ip(0, 2)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, 2)
            if self.rect.colliderect(rect):
                self.rect.bottom = rect.top
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-2, 0)  
            self.turned = False
            if self.rect.colliderect(rect):
                self.rect.left = rect.right 
        if key[pygame.K_RIGHT]:
            self.turned = True
            self.rect.move_ip(2, 0)
            if self.rect.colliderect(rect):
                self.rect.right = rect.left 
   
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_w:
            self.rect.right = screen_w
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_h:
            self.rect.bottom = screen_h           
