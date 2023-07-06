from state import State
from rect import Shape
from player import Player
from enemy import Enemy
import pygame
import random
import math

class FarmScreen(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game = game
        self.background = pygame.image.load("BACKGROUND_CITY.xcf")

       # self.screen = self.game.screen
        self.cropTypes = [ "MINT.xcf", "ROSE.xcf", "Lavender.xcf"]
        self.crops = ["mint", "rose", "lavender"]
        self.types = []
        self.xLocation = []
        self.yLocation = []
        self.cropRects = []
        self.cropLocations = []
        self.img = ("doctor.xcf")
        self.size = 5
        self.radius = 10
        self.makeCrops(10)
        self.enemy = Enemy()
        self.enemy.makeEnemies(4)
        self.circlPosX = []
        self.circlePosY = []
        self.circleArray = []
        self.inInventory = False
        self.cropTimers = []
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
        if actions["q"]:
            #self.gathered()
            self.checkOverlap()
        if actions["tab"]:
            if self.inInventory:
                self.inInventory = False
            else:
                self.inInventory = True
        #if q_pressed:    
           # self.player.harvestPlant(self.cropLocations, self.types, self.crops, self.size)
            #self.harvest(self.player.rect.left +25, self.player.rect.top + 25)
            
            

    def render(self, display):
        display.fill((211,211,211))
        pygame.display.set_caption("BLACK PLAGUE CITY")
        display.blit(pygame.transform.scale(self.background, (1280, 720)), (0, 0))
        #pygame.draw.rect(screen, (0, 0, 255), self.rect)
        self.putCrops(display)
        self.enemy.putEnemies(display)
        #self.enemy.moveEnemies()
        #self.enemy.movenum2(self.player)
        #self.enemy.move_towards_player(self.player)
        ##FIX ME: MAKE LITTLE MAN RENDER AS DOCTOR2.XCF IF GOING RIGHT
        self.enemyMovement()
        self.player.draw(display, "doctor.xcf")
        self.player.displayHealthGold(self.game.screen)
        if self.inInventory:
            self.player.showInventory(display)
        if self.size == 0:
            self.resetCrops(display)
        self.enemy.randomSpawnEnemies()
        self.randomSpawnCrops()



    def makeCrops(self, size):
        self.size = size
        for i in range(self.size):
            type = random.randint(0, 2)
            self.types.append(type)
            xx = random.randint(0, 1180)
            yy = random.randint(30, 620)
            self.xLocation.append(xx)
            self.yLocation.append(yy)
            self.cropRects.append(pygame.rect.Rect(xx, yy, 50, 50))
            self.cropLocations.append([xx, yy])
            
 
    def putCrops(self, display):
        for x in range(self.size):
            img_surface = pygame.image.load(self.cropTypes[self.types[x]]).convert_alpha()
            conformed = pygame.transform.scale(img_surface, (50, 50))
            display.blit(conformed, self.cropRects[x])

    def resetCrops(self, size):
        self.makeCrops(self, size)
        self.putCrops(self, self.game.screen)


    def checkOverlap(self):
        for x in range(self.size):
            if self.cropRects[x].colliderect(self.player.getRect()):
                self.cropRects.pop(x) 
                self.player.addToInventory(self.crops[self.types[x]])
                self.types.pop(x) #started going slow when i added this
                self.size -= 1
                self.cropTimers.append(pygame.time.get_ticks())
                break
        for x in range(len(self.enemy.enemyRects)):
            if self.enemy.enemyRects[x].colliderect(self.player.getRect()):
                self.player.increaseGold(10)
                self.enemy.enemyRects.pop(x) 
                self.enemy.numEnemies -= 1
                self.enemy.Locations.pop(x)
                self.enemy.enemySpawnTimes.append(pygame.time.get_ticks())

                break

    def enemyMovement(self):

#FIXME add image for the flipped rat based on direction
#FIXME make movements less jagged
        for x in range(len(self.enemy.enemyRects)):
            x_distance = abs(self.player.rect.x - self.enemy.enemyRects[x].x)
            y_distance = abs(self.player.rect.y - self.enemy.enemyRects[x].y)
            if x_distance <= 200 and y_distance <= 200:
                self.enemy.move_towards_player(self.player, x)
            else:
            #x or y
                numero = random.randint(0, 1)
            #direction
                numerodos = random.randint(0, 1)
                if numero == 0:
                    if numerodos ==0:
                        self.enemy.enemyRects[x].left += 3
                    else: 
                        self.enemy.enemyRects[x].left -= 3
                else:
                    if numerodos == 0:
                        self.enemy.enemyRects[x].top += 3
                    else:
                        self.enemy.enemyRects[x].top -= 3

                if self.enemy.enemyRects[x].left < 0:
                    self.enemy.enemyRects[x].left = 0
                if self.enemy.enemyRects[x].right > 1280:
                    self.enemy.enemyRects[x].right = 1280
                if self.enemy.enemyRects[x].top < 0:
                    self.enemy.enemyRects[x].top = 0
                if self.enemy.enemyRects[x].bottom > 720:
                    self.enemy.enemyRects[x].bottom = 720  


    def randomSpawnCrops(self):
#FIXME rat spawn location not to spawn on person
#FIXME screen slows down a lot
#FIXME list index outta range
        if len(self.cropTimers) != 0:
            for x in range(len(self.cropTimers)):
                currentTime = math.floor((pygame.time.get_ticks() - self.cropTimers[x])/1000)
                if currentTime > 10:
                    xx = 1200
                    yy = random.randint(100, 620)
                    self.cropRects.append(pygame.rect.Rect(xx, yy, 50, 50))
                    self.size +=1
                    self.cropTimers.pop(x)
    



#Crop class for the purpose of readability and easy access to deleting and putting crops
#FIXME fix the reset function to do it with time