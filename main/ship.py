import pygame

class Ship:
    """Class for ship to shoot bullets"""
    
    def __init__(self,ai_game) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image anf get its 'rect'. rectangle for efficent game processsing
        self.image = pygame.image.load('c:/Users/Conor/alien_invaders_game/main/images/millenium_falcon.bmp') # relative path main\images\ship.bmp 
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Draw the ship ay its current location '''
        self.screen.blit(self.image, self.rect)