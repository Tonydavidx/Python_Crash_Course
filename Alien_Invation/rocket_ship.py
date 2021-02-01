import pygame

class Rock:
    """ a class to manage rocket """
    def __init__(self, rocket_game):
        """ Initialize the ship and set its starting postions """
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()

        # load the rocket image and get its rect
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()

        # start new rocket in center of the screen
        self.rect.center = self.screen_rect.center

    def blit_rocket(self):
        """ draw the rocket at its currennt location """
        self.screen.blit(self.image, self.rect)    

