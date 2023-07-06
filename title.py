from state import State
from rect import Shape
from mainscreen import Main
from rect import Shape
import pygame

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game = game
        #background
        self.background = pygame.image.load("title.xcf")
        self.littleGuy = pygame.image.load("doctor.xcf")
        self.startImg = "Start.xcf"
        
        #button set up
        self.font = pygame.font.SysFont(None, 30)
        self.BLACK = (0, 0, 0)


    def update(self, actions):
        x, y = pygame.mouse.get_pos()
        
        if actions["quit"]:
            self.game.playing = False
            self.game.running = False
        if actions["started"]:
            #new_state = Main(self.game)
            #new_state.enter_state()
            self.game.mainScreen.enter_state()
        if actions["credits"]:
            self.game.creditsScreen.enter_state()
        if actions["controls"]:
            self.game.controlsScreen.enter_state()
        #print(x, y)
        #x, y = pygame.mouse.get_pos()            
        #for event in pygame.event.get():
         #   if event.type == pygame.MOUSEBUTTONDOWN:
          #      print(0)
           #     if(abs(x - 1280/2) <= 150 and abs(y- 360) <= 45):
            #        self.playing = False
             #       self.running = False
              #  if(abs(x - 1280/2) <= 150 and abs(y- 240) <= 45):
               #     print("main")
                #    self.game.mainScreen.enter_state()
                #if(abs(x - 1280/2) <= 150 and abs(y- 480) <= 45):
                #    self.game.creditsScreen.enter_state()
                #if(abs(x - 1280/2) <= 150 and abs(y- 600) <= 45):
                #    self.game.controlsScreen.enter_state()


        #self.game.reset_keys()
       
    
    def render(self, display):
        display.fill((211,211,211))
        pygame.display.set_caption("POOP WINDOW")
        display.blit(pygame.transform.scale(self.background, (1280, 720)), (0, 0))
        #display.blit(pygame.transform.scale(self.background, (1280, 720)), (0, 0))
        #self.makeButton(self.game.screen, self.font, "START", self.BLACK, self.game.SCREEN_WIDTH/2, 240)
        img_surface = pygame.image.load(self.startImg).convert_alpha()
        rectum = pygame.rect.Rect(self.game.SCREEN_WIDTH/2 - 300/2, 240 - 90/2, 300, 90)
        #display.blit(img_surface, rectum )
        display.blit(pygame.transform.scale(img_surface, (300, 90)), rectum)
        self.makeButton(self.game.screen, self.font, "QUIT", self.BLACK, self.game.SCREEN_WIDTH/2, 360)
        self.makeButton(self.game.screen, self.font, "CREDITS", self.BLACK, self.game.SCREEN_WIDTH/2, 480)
        self.makeButton(self.game.screen, self.font, "CONTROLS", self.BLACK, self.game.SCREEN_WIDTH/2, 600)
     
        
        #for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONUP:
        mousePos = pygame.mouse.get_pos()
        Shape.drawCircle(Shape, self.game.screen, (211, 211, 211), mousePos, 10)

        #for event in pygame.event.get():
            
            #if event.type == pygame.MOUSEBUTTONDOWN:

        #self.game.draw_text(display, "Game States Demo", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2 )
    def makeButton(self, screen, font, text, color, x, y):
        #Shape.drawRect(Shape, screen, (screen_w / 2) - 150/2, (screen_h / 2) - 90/2, 150, 90, (175,175,175))
        Shape.drawRect(Shape, screen, x - 300/2, y - 90/2, 300, 90, (175,175,175))
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        
        screen.blit(text_surface, text_rect)