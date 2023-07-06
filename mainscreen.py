from state import State
from rect import Shape
from player import Player
from farmland import FarmScreen
import pygame
from npc import NPC
import random
from enemy import Enemy
import time
import math

class Main(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.currentx = 0
        self.currenty = 0
        self.game = game
        self.SCREEN_WIDTH =1280
        self.background = pygame.image.load("BACKGROUND.xcf")
        self.show = False
        self.player = Player()
        self.img = ("doctor.xcf")
        self.xlocation = [100, 250, 400] #keeps track of locations
        self.npcVoiceLines =["beware the rats", "please im hungry", "this might be my last day.."]
        self.enemies = Enemy()
        self.bing = False
        self.atMarket = False
        self.atBrew = False
        self.marketActions = {"itemOne": False, "itemTwo": False, "itemThree": False}
        self.inInventory = False
        self.table = {"first" : False, "second" : False, "third" : False}
        self.npc1 = NPC(self.xlocation[0], 520, 100, 100, "NPC1.xcf", self.game.screen)
        self.npc2 = NPC(self.xlocation[1], 520, 100, 100, "NPC2.xcf", self.game.screen)
        self.npc3 = NPC(self.xlocation[2], 520, 100, 100, "NPC3.xcf", self.game.screen)   
        self.counter = 1

        self.brewQueue = []
        self.timers = []
        self.medicines = ["MINT.xcf", "ROSE.xcf", "Lavender.xcf"]




        #market purposes
        #images of items       
        self.img_surface1 = pygame.image.load("Ointment.xcf").convert_alpha()
        self.img_surface2 = pygame.image.load("Potion.xcf").convert_alpha()
        self.img_surface3 = pygame.image.load("Honey.xcf").convert_alpha()
        self.rect1 = pygame.rect.Rect(1280/2 -250, 720/2, 100, 100)
        self.rect2 = pygame.rect.Rect(1280/2 - 50, 720/2, 100, 100)
        self.rect3 = pygame.rect.Rect(1280/2 + 150, 720/2, 100, 100)
        self.itemPrices = [10, 5, 15]
        self.marketList = {"ointment": self.itemPrices[0], "potion": self.itemPrices[1], "honey": self.itemPrices[2]}
        self.itemLocations = [self.rect1, self.rect2, self.rect3]
        self.itemSelected = [False, False, False]



        self.coinimg = "COIN.xcf"
        self.font = pygame.font.SysFont(None, 30)
        self.images = ["Honey.xcf", "Potion.xcf", "Ointment.xcf", "Lavender.xcf", "ROSE.xcf", "MINT.xcf", "medicine1.xcf", "medicine2.xcf", "medicine3.xcf"]
        self.recipeImages = ["medicine1gray.xcf", "medicine2gray.xcf", "medicine3gray.xcf"]
        self.recipeNames = ["Penecillin", "Electuary", "Ointment"]
        self.recipeIngredients = ["Ointment X 1\nMint X 5\n Lavender X 1\nRose X 1", "Honey X 1\nLavender X 4\n Rose X 2", "Honey x 2\nMint X 3\nRose X 3"]
        self.recipeIngredients2 = ["Ointment X 1\nMint X 5\n Lavender X 1\nRose X 1", "Honey X 1\nLavender X 4\n Rose X 2", "Honey x 2\nMint X 3\nRose X 3"]
        self.recipeIngredients3 = ["Ointment X 1\nMint X 5\n Lavender X 1\nRose X 1", "Honey X 1\nLavender X 4\n Rose X 2", "Honey x 2\nMint X 3\nRose X 3"]
        self.brewing = False
        self.mainscreenClock = pygame.time.Clock()



            
    def update(self, actions):
        
        key = pygame.key.get_pressed()
        #self.player.move(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT)
        if not(self.atMarket or self.inInventory or self.atBrew):
            self.player.moveMain(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT, self.xlocation)
            #self.player.moveWithCollides(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT, self.npc1.rect)
            #self.player.moveWithCollides(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT, self.npc2.rect)
            #self.player.moveWithCollides(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT, self.npc3.rect)

        if self.player.rect.right > 1279:
            #print("FARM")
            self.game.farmScreen.enter_state()
            self.atMarket = False
        if actions["tab"]:
            if self.inInventory:
                self.inInventory = False
            else:
                self.inInventory = True
        if actions["w"]:  
            if self.atBrew:
                self.atBrew = False
            else:
                if self.player.rect.left < 165 and self.player.rect.top > 230 and self.player.rect.top < 390: #and self.player.rect.top < 100
                    self.atBrew = True
            if self.atMarket:
                #if actions["w"]:
                self.atMarket = False
                #print("at market")
            else:
                if self.player.rect.left < 1000 and self.player.rect.right > 830 and self.player.rect.top < 170: #and self.player.rect.top < 100
                    self.atMarket = True
            if actions["up"]:
                self.counter -= 1
            if actions["down"]:
                self.counter += 1    
            
        #if actions["q"]:
            #if actions["up"]:

            #if actions["down"]:    
            
            #if actions["right"]:
            
            #if actions["left"]:

        self.game.reset_keys()
    def render(self, display):
        
        display.fill((211,211,211))
        pygame.display.set_caption("CITY OUTSKIRTS")
        display.blit(pygame.transform.scale(self.background, (1280, 720)), (0, 0))
        #pygame.draw.rect(screen, (0, 0, 255), self.rect)
        self.player.draw(display, self.img)
        
        self.npc1.draw()
        self.npc1.talk(self.npcVoiceLines[0])
        self.npc2.draw()
        self.npc2.talk(self.npcVoiceLines[1])
        self.npc3.draw()
        self.npc3.talk(self.npcVoiceLines[2])

        #self.npc1.move() 
        #self.npc2.move() 
        #self.npc3.move() 

        if self.inInventory:
           self.player.showInventory(self.game.screen)
        #FIXME fix inventory
        #MARKET:
       # Shape.drawRect(Shape, self.game.screen, 1085, 50, 100, 50, (175,175,175))
        if self.atMarket:
            self.showMarketScreen(self.game.screen, self.game.actions)

        if self.atBrew:
            self.showBrewScreen(self.game.screen, self.game.actions)

        self.player.displayHealthGold(self.game.screen)
        #self.npc1 = NPC.__init__(NPC, 200, 200, 50, 50, self.img, self.game.screen, "YUHHHHH")
        #self.npc1.draw(NPC)
        #self.npc1.talk(NPC)
        Shape.drawRect(Shape, display, 0, 0, 175, 55, (0, 0, 0))
        Shape.drawRect(Shape, display, 0, 0, 170, 50, (150, 75, 0))
        Shape.drawRect(Shape, display, 55, 0, 10, 50, (0, 0, 0))
        if len(self.timers) > 0:
            self.renderBrewQueue(display)


    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)



    def showBrewScreen (self, screen, actions):

        Shape.drawRect(Shape, self.game.screen, 1280/2 - 400, 720/2 -250, 800, 600, (250,250,250))
        

        locationCounter = -250

        for x in range(3): 
            text_surface = self.font.render(self.medicines[x], True, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (1280/2+ locationCounter +50, 720/2 + 150)

            screen.blit(text_surface, text_rect)
            locationCounter += 200





        screen.blit(self.img_surface1, self.rect1)
        screen.blit(self.img_surface2, self.rect2)
        screen.blit(self.img_surface3, self.rect3)

#FIXME: if inventory available, images change to color version image  
                #Event handling
        x, y = pygame.mouse.get_pos()
        #for event in pygame.event.get():
        if(abs(x - self.SCREEN_WIDTH/2 +200) <= 50 and abs(y- 410) <= 50):
            self.itemSelected[0] = True
        if(abs(x - self.SCREEN_WIDTH/2) <= 50 and abs(y- 410) <= 50):
            self.itemSelected[1] = True
        if(abs(x - self.SCREEN_WIDTH/2 - 200) <= 50 and abs(y- 410) <= 50):
            self.itemSelected[2] = True

        for x in range(3):
            if self.itemSelected[x]:
                self.itemLocations[x].top = 720/2 -100
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.addToBrewQueue(x)
                        #self.player.addToInventory(list(self.marketList.keys()).index(self.itemPrices[x]))
            else:
                self.itemLocations[x].top = 720/2
        
        #reset
        for x in range(3):
            self.itemSelected[x] = False
#FIXME: add bar timer?


    def showMarketScreen(self, screen, actions):
        
        self.marketRect = pygame.rect.Rect(1280/2 -400, 720/2 -250, 800, 500)
        Shape.drawRect(Shape, self.game.screen, 1280/2 - 400, 720/2 -250, 800, 500, (250,250,250))
        

        #item prices        
        locationCounter = -250
        img_surface = pygame.image.load(self.coinimg).convert_alpha()
        transformed_img = pygame.transform.scale(img_surface, (50, 50))

        for x in range(3): 
            #prices
            text_surface = self.font.render("X " + str(self.itemPrices[x]), True, (0,0,0))
            img_rect = transformed_img.get_rect()
            text_rect = text_surface.get_rect()
            text_rect.center = (1280/2+ locationCounter +70, 720/2 + 125)
            img_rect.center = (1280/2 +locationCounter +30, 720/2 +125)
            
            screen.blit(transformed_img, img_rect)
            screen.blit(text_surface, text_rect)
            locationCounter += 200




        screen.blit(self.img_surface1, self.rect1)
        screen.blit(self.img_surface2, self.rect2)
        screen.blit(self.img_surface3, self.rect3)

        #Event handling
        x, y = pygame.mouse.get_pos()
        if(abs(x - self.SCREEN_WIDTH/2 +200) <= 50 and abs(y- 410) <= 50):
            self.itemSelected[0] = True
        if(abs(x - self.SCREEN_WIDTH/2) <= 50 and abs(y- 410) <= 50):
            self.itemSelected[1] = True
        if(abs(x - self.SCREEN_WIDTH/2 - 200) <= 50 and abs(y- 410) <= 50):
            self.itemSelected[2] = True

        for x in range(3):
            if self.itemSelected[x]:
                self.itemLocations[x].top = 720/2 -100
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
#FIXME put the +1 so they know it worked or highight the gold
                        text_surface = self.font.render("+1", True, (0,0,0))
                        text_rect = text_surface.get_rect()
                        text_rect.center = (self.itemLocations[x].left + 50, 360 - 150)
                        screen.blit(text_surface, text_rect)
                        self.player.decreaseGold(self.itemPrices[x])
                        #pygame.time.wait(2000)
            else:
                self.itemLocations[x].top = 720/2
            
        #reset
        for x in range(3):
            self.itemSelected[x] = False


    def generateNpcRequests(self):

        #two diff ways to do it, time in game or difficulty with brew time
        amount = 0
        rando = random.randint(0, 99)
        if rando < 19:
            amount = 3
        elif rando < 39:
            amount = 2
        else: 
            amount = 1
        #generate number based on time in game
        num = 0
        mins = pygame.time.get_ticks()/60000 
        if mins <= 2:
            num = 1
        elif mins <= 4:
            num = 2
        else:
            num = 3

        for x in range(3):
            #generate random medicinal item
            medicine = random.randint(0, 2)
            self.npcVoiceLines[x] = str(num) + self.medicines[medicine]

    def addToBrewQueue(self, num):
        self.brewQueue.append(self.medicines[num])
        print(len(self.brewQueue))
        self.timers.append(pygame.time.get_ticks())


    def renderBrewQueue(self, screen):
        currentTime = math.floor((pygame.time.get_ticks() - self.timers[0])/1000)
        if currentTime < 5:
            text_surface1 = self.font.render(str(5 - currentTime), True, (0,0,0))
            text_surface2 = self.font.render("brewing..", True, (0,0,0))
            text_rect1 = text_surface1.get_rect()
            text_rect2 = text_surface2.get_rect()
            text_rect2.w, text_rect2.h = 100, 50
            text_rect2.center = (120, 40)
            temp = pygame.rect.Rect(0, 0, 70, 50)
            img_surface = pygame.transform.scale(pygame.image.load(self.brewQueue[0]).convert_alpha(), (50, 50))
            screen.blit(img_surface, temp)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)


        else:
            self.player.addToInventory("honey")
            self.brewQueue.pop(0)
            self.timers.pop(0)
            if len(self.timers) > 0:
                self.timers[0] = pygame.time.get_ticks()
    


    #implement escape button or whatevs to go back to title
    #we need some images for npc and enemies. gimp or internet

