import pygame

class Ship:
    """Class for ship to shoot bullets"""
    
    def __init__(self,ai_game) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load ship image anf get its 'rect'. rectangle for efficent game processsing
        self.image = pygame.image.load('c:/Users/Conor/alien_invaders_game/main/images/millenium_falcon.bmp') # relative path main\images\ship.bmp 
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ships exact horizontal position
        self.x = float(self.rect.x) #floats offers more granularity for movemment


        #creating a movemenet flag: start with a ship thats not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        ''' update the ships position based on the movement flag '''
        #update the ships x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed #continuous movement when the KEYDOWN is pressed/ if TRUE
 
        if self.moving_left and self.rect.left > 0 :
                    self.rect.x -= self.settings.ship_speed  #continuous movement when the KEYDOWN is pressed/ if TRUE
 
        #update rect oject from self.x
        #this adds only the integer position instead of the more accurate react postion which is fine for displaying purposes 
        self.rect.x= self.x



    def blitme(self):
        '''Draw the ship ay its current location '''
        self.screen.blit(self.image, self.rect)