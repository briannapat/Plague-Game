from state import State
from rect import Shape
from player import Player
from enemy import Enemy
import pygame
import random

class FarmScreen(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game = game
        self.background = pygame.image.load("BACKGROUND_CITY.xcf")

       # self.screen = self.game.screen
        self.cropTypes = [ "MINT.xcf", "ROSE.xcf", "Lavender.xcf"]
        self.types = []
        self.xLocation = []
        self.yLocation = []
        self.img = ("doctor.xcf")
        self.size = 10
        self.radius = 10
        self.makeCrops(10)
        self.enemy = Enemy()
        self.enemy.makeEnemies()
        self.circlPosX = []
        self.circlePosY = []
        self.circleArray = []
        #self.rect = pygame.Rect(50, 100, 50, 50)



    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
            self.player = self.prev_state.player
            self.player.resetLocation(5, True)
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()
        self.player.resetLocation(1265, False)


    def update(self, actions):
        key = pygame.key.get_pressed()
        self.player.moveFarm(key, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT)
        if self.player.rect.left < 1:
            self.exit_state()
        q_pressed = actions["q"]     
        #if q_pressed and not self.was_pressed:    
            #self.harvest(self.player.rect.left +25, self.player.rect.top + 25)
        #self.was_pressed = q_pressed    
            
            

    def render(self, display):
        display.fill((211,211,211))
        pygame.display.set_caption("BABY MAKING WINDOW")
        display.blit(pygame.transform.scale(self.background, (1280, 720)), (0, 0))
        #pygame.draw.rect(screen, (0, 0, 255), self.rect)
        self.putCrops(display, "MINT.xcf")
        self.enemy.putEnemies(display)
        self.enemy.moveEnemies()
        ##FIX ME: MAKE LITTLE MAN RENDER AS DOCTOR2.XCF IF GOING RIGHT
        self.player.draw(display, "doctor.xcf")
        self.player.displayHealthGold(self.game.screen)



    def makeCrops(self, size):
        self.size = size
        for i in range(self.size):
            type = random.randint(0, 2)
            self.types.append(type)
            self.xLocation.append(random.randint(0, 1180))
            self.yLocation.append(random.randint(0, 620))
            
 
    def putCrops(self, display, img):
        for x in range(self.size):
           # Shape.drawCircle(Shape, screen, (255,255,255), (self.xLocation[x], self.yLocation[x]), self.radius)
           # self.circlePosX = self.xLocation[x]
           # self.circlePosY = self.yLocation[x]
            #img_surface = pygame.image.load(self.cropTypes[self.types[x]]).convert_alpha()
            #Shape.drawRect(Shape, display, self.xLocation[x], self.yLocation[x], 50, 50, (255,255,255)) 
            img_surface = pygame.image.load(self.cropTypes[self.types[x]]).convert_alpha()
            display.blit(img_surface, (self.xLocation[x], self.yLocation[x]))
        
    def gather(self, o, y):
        for x in range(self.size):
            #if key[pygame.K_q] and abs(Player.getX(peewee) -self.xLocation[x]) <= 11 and abs(Player.getY(peewee) - self.yLocation[x]) <= 11:
            #print(o)
            #print(y)
            #print(self.xLocation)
            #print(self.yLocation)
            #CHANGE BACK TO + 10
            if (o >= self.xLocation[x]-15 and o <= self.xLocation[x] + 15) and (y >= self.yLocation[x]-15 and y<= self.yLocation[x] +15):
                print("pop")
                self.xLocation.remove(self.xLocation[x])
                self.yLocation.remove(self.yLocation[x])
                self.size -= 1
                print(self.size)
                #putCrops(screen)
                break


    def resetCrops(self, size):
        self.makeCrops(self, size)
        self.putCrops(self, self.game.screen, "MINT.xcf")



    #change crop locations to not spawn on the road or houses

        #self.enemies.makeEnemies()
        #self.enemies.putEnemies(self.game.screen)
        #self.enemies.moveEnemies()
