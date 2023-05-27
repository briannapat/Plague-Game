import pygame
from player import Player
from rect import Shape
from farm import Farm
from mainscreen import Main
from title import Title
from farmland import FarmScreen                                     
from credits import Credits

class Real():
    def __init__(self):
            pygame.init()
            self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 1280, 720
            self.GAME_W,self.GAME_H = 480, 270
            self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
            self.mainScreen = Main(self)
            self.farmScreen = FarmScreen(self)
            self.creditsScreen = Credits(self)
           
            self.running, self.playing = True, True
            self.actions = {"back": False, "escape": False, "w": False, "quit": False, "tab": False,"credits": False, "started": False, "left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False, "q" : False}
            self.state_stack = []   
            self.background = pygame.image.load("BACKGROUND.xcf")
            self.littleGuy = pygame.image.load("doctor.xcf")

    def get_events(self):
        x, y = pygame.mouse.get_pos()            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(abs(x - self.SCREEN_WIDTH/2) <= 150 and abs(y- 360) <= 45):
                    print("DOME")
                    #if (x >= 490 and x <= 790) and (y >= 320 and y <= 410):
                    self.actions["quit"] = True
                if(abs(x - self.SCREEN_WIDTH/2) <= 150 and abs(y- 240) <= 45):
                    #if (x >= 490 and x <= 790) and (y >= 240 and y <= 410):
                    self.actions['started'] = True 
                if(abs(x - self.SCREEN_WIDTH/2) <= 150 and abs(y- 480) <= 45):
                    self.actions['credits'] = True
                if(abs(x - self.SCREEN_WIDTH/2) <= 150 and abs(y- 360) <= 45):
                    print("back")
                    self.actions['back'] = True    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = True
                    #self.playing = False
                    #self.running = False
                if event.key == pygame.K_TAB:
                    self.actions['tab'] = True
                if event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_q:
                    self.actions["q"] = True
                    #self.farmScreen.harvest(x, y)
                if event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_w:
                    self.actions['w'] = True
                if event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_p:
                    self.actions['action1'] = True
                if event.key == pygame.K_o:
                    self.actions['action2'] = True    
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True  
            if event.type == pygame.MOUSEBUTTONUP:
                self.actions["quit"] = False
                self.actions['started'] = False
                self.actions['credits'] = False
                self.actions['back'] = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB:
                    self.actions['tab'] = False
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_w:
                    self.actions['up'] = False
                if event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_p:
                    self.actions['action1'] = False
                if event.key == pygame.K_q:
                    self.actions["q"] = False    
                if event.key == pygame.K_o:
                    self.actions['action2'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False  

            #if pygame.mouse.get_pressed()[0] and mouse

    def update(self):
        self.state_stack[-1].update(self.actions)

    def render(self):
        self.state_stack[-1].render(self.screen)
        # Render current state to the screen
        #self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()
    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def game_loop(self):
        while self.playing:
            #self.get_dt()
            self.get_events()
            self.update()
            self.render()


#game = Game()
#game.__init__()
#game.main_loop()

g = Real()
t = Title(g)
c = Credits(g)
g.state_stack.append(t)
while g.running:
    g.game_loop()

#timer pass as argument
#Have reset function in farm screen reset per a certain condition
#Have reset function rest crop locations and amounts and despawn based on timer
#Have rats spawn separately from crops 