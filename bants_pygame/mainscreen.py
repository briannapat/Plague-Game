from state import State
from rect import Shape
from player import Player
from farmland import FarmScreen
import pygame
from npc import NPC
import random
from enemy import Enemy

class Main(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.currentx = 0
        self.currenty = 0
        self.game = game
        self.background = pygame.image.load("BACKGROUND.xcf")
        self.show = False
        self.player = Player()
        self.img = ("doctor.xcf")
        self.xlocation = [] #keeps track of locations
        self.ylocation = [] #keeps track of locations
        self.npcVoiceLines =["beware the rats", "please im hungry", "this might be my last day.."]
        self.enemies = Enemy()
        self.bing = False
        self.atMarket = False
        self.inInventory = False
        self.rectums = [[1085-50 + 15, 170+50, 150, 75], [1085-50 + 15, 240+70, 150, 75], [1085-50 + 15, 310+90, 150, 75]]
        self.table = {"first" : False, "second" : False, "third" : False}
        #set locations
        for x in range(3):
            xx = random.randint(100, 540)
            yy = random.randint(100, 600)
            self.xlocation.append(xx)
            self.ylocation.append(yy)
            #self.npc1 = NPC.__init__(NPC, xx, yy, 50, 50, self.img, self.game.screen, self.npcVoiceLines[x])
        self.npc1 = NPC(self.xlocation[0], 520, 100, 100, "NPC1.xcf", self.game.screen, self.npcVoiceLines[0])
        self.npc2 = NPC(self.xlocation[1], 520, 100, 100, "NPC2.xcf", self.game.screen, self.npcVoiceLines[1])
        self.npc3 = NPC(self.xlocation[2], 520, 100, 100, "NPC3.xcf", self.game.screen, self.npcVoiceLines[2])   
        self.counter = 1
            
    def update(self, actions):
        
        key = pygame.key.get_pressed()
        #self.player.move(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT)
        if not(self.atMarket or self.inInventory):
            self.player.moveMain(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT, self.xlocation)
            #self.player.moveWithCollides(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT, self.npc1.rect)
            #self.player.moveWithCollides(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT, self.npc2.rect)
            #self.player.moveWithCollides(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT, self.npc3.rect)

        if self.player.rect.right > 1279:
            #print("FARM")
            self.game.farmScreen.enter_state()
            self.atMarket = False
        if actions["tab"]:
            self.inInventory = True
            self.player.loseHealth()
        if actions["w"]:  
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
        pygame.display.set_caption("BLACK PLAGUE CITY")
        display.blit(pygame.transform.scale(self.background, (1280, 720)), (0, 0))
        #pygame.draw.rect(screen, (0, 0, 255), self.rect)
        self.player.draw(display, self.img)
        
        self.npc1.draw()
        self.npc1.talk()
        self.npc2.draw()
        self.npc2.talk()
        self.npc3.draw()
        self.npc3.talk()

        #self.npc1.move() 
        #self.npc2.move() 
        #self.npc3.move() 



        if self.inInventory:
           self.player.showInventory(self.game.screen)
           self.inInventory = False

        #FIXME fix inventory
        #MARKET:
       # Shape.drawRect(Shape, self.game.screen, 1085, 50, 100, 50, (175,175,175))
        if self.atMarket:
            self.showMarketScreen(self.game.screen, self.game.actions)

        self.player.displayHealthGold(self.game.screen)
        #self.npc1 = NPC.__init__(NPC, 200, 200, 50, 50, self.img, self.game.screen, "YUHHHHH")
        #self.npc1.draw(NPC)
        #self.npc1.talk(NPC)

        


    #def slash(self):
        #if (self.player.rect.left +50)

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)




    def showMarketScreen(self, screen, actions):
        #Shape.drawRect(Shape, self.game.screen, 1085-50, 100+50, 180, 400, (250,250,250))
        #Shape.drawRect(Shape, self.game.screen, 1085-50 + 15, 170+50, 150, 75, (0,10,0))
        #Shape.drawRect(Shape, self.game.screen, 1085-50 + 15, 240+70, 150, 75, (0,20,0))
        #Shape.drawRect(Shape, self.game.screen, 1085-50 + 15, 310+90, 150, 75, (0,30,0))
        Shape.drawRect(Shape, self.game.screen, 1280/2 - 400, 720/2 -250, 800, 500, (250,250,250))

            #EVENT HANDLING
       
        img_surface1 = pygame.image.load("Ointment.xcf").convert_alpha()
        img_surface2 = pygame.image.load("Potion.xcf").convert_alpha()
        img_surface3 = pygame.image.load("Honey.xcf").convert_alpha()
        rect1 = pygame.rect.Rect(1280/2 -400, 720/2, 100, 100)
        rect2 = pygame.rect.Rect(1280/2 -200, 720/2, 100, 100)
        rect3 = pygame.rect.Rect(1280/2, 720/2, 100, 100)

        screen.blit(img_surface1, rect1)
        screen.blit(img_surface2, rect2)
        screen.blit(img_surface3, rect3)

        if actions["up"]:
                self.counter -= 1
        if actions["down"]:
            self.counter += 1   
                         
        if self.counter >= 3:
            self.counter = 2
        if self.counter < 0:
            self.counter = 1
            
        if self.counter == 2:
            self.table["third"] = True
            self.table["second"] = False
            self.table["first"] = False

        if self.counter == 1:
            self.table["second"] = True
            self.table["third"] = False
            self.table["first"] = False

        
        if self.counter == 0:
            self.table["first"] = True
            self.table["third"] = False
            self.table["second"] = False

        for ret in self.rectums:
            tempRect = pygame.Rect(ret[0], ret[1], ret[2], ret[3]) 

            if self.counter==0 and self.table["first"]:
                pygame.draw.rect(screen, (0, 250, 0), tempRect)
                print("first")
            if self.counter==1 and self.table["second"]:
                pygame.draw.rect(screen, (0,250,0), tempRect)
                #print("second")
            if self.counter==2 and self.table["third"]:
                pygame.draw.rect(screen, (0,250,0), tempRect)
                print("third")
            else:
                pygame.draw.rect(screen, (0, 0, 250), tempRect)    
        
        
        # if key up counter - 1
        # self.table[counter] == True

        #keep a typle of locations 
        # hash table of truth values for selected
        # for loop to iterate through to reset

        #if actions["down"]:


        
    #implement escape button or whatevs to go back to title
    #we need some images for npc and enemies. gimp or internet
 
class Projectile():
    def __init__(self, x, y):
        self.x, self.y, self.radius = x ,y, 5

