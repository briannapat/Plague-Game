from state import State
from rect import Shape
from player import Player
from farmland import FarmScreen
import pygame

class Credits(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game = game
        self.background = pygame.image.load("title.xcf")
        self.font = pygame.font.SysFont(None, 30)
        self.BLACK = (0, 0, 0)

    def render(self, display):
        display.fill((211,211,211))
        pygame.display.set_caption("CREDDDDITS BABBBYY")
        display.blit(pygame.transform.scale(self.background, (1280, 720)), (0, 0))
        #pygame.draw.rect(screen, (0, 0, 255), self.rect)
        self.makeButton(self.game.screen, self.font, "PATTEN AND HARBAN", self.BLACK, self.game.SCREEN_WIDTH/2, 480)
        self.makeButton(self.game.screen, self.font, "BACK", self.BLACK, self.game.SCREEN_WIDTH/2, 360)

    def update(self, actions):
        if actions["back"]:
            self.game.creditsScreen.exit_state()        

    def makeButton(self, screen, font, text, color, x, y):
        #Shape.drawRect(Shape, screen, (screen_w / 2) - 150/2, (screen_h / 2) - 90/2, 150, 90, (175,175,175))
        Shape.drawRect(Shape, screen, x - 300/2, y - 90/2, 300, 90, (175,175,175))
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)
