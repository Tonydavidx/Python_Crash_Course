import sys
import pygame
from rocket_ship import Rock

class Rocket:
    """ a game that begins with a rocket at the center of the screen and moves in arrow keys direction """
    def __init__(self):
        pygame.init()
        self.settings()
        self.screen = pygame.display.set_mode((900,700))
        pygame.display.set_caption('Rocket')

        self.rocket_ship = Rock(self)


    def run_game(self):
        """ a run function to start the game """
        while True:
            self.check_events()
            self.screen.fill(self.bg_color)
            self.rocket_ship.blit_rocket()

    def check_events(self):
        """ check events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # make the most recently drawn screen visible
        pygame.display.flip()        
                

    def settings(self):
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (200, 200, 200)    

if __name__ == '__main__':
    game = Rocket()
    game.run_game()   
         