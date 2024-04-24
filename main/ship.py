import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        #load ship image anf get its 'rect'. rectangle for efficent game processsing
        self.image = pygame.image.load('c:/Users/Conor/alien_invaders_game/main/images/millenium_falcon.bmp') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self.center.
        self.rect.centerx = self.center
                
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


    '''    older code


class Ship:
    """Class for ship to shoot bullets"""
    def __init__(self,ai_game,screen):
        
        self.screen = screen
        self.settings = ai_game.settings
        
        #load ship image anf get its 'rect'. rectangle for efficent game processsing
        self.image = pygame.image.load('c:/Users/Conor/alien_invaders_game/main/images/millenium_falcon.bmp') # relative path main\images\ship.bmp 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    
        #self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ships exact horizontal position
        self.center = float(self.rect.centerx) #floats offers more granularity for movemment


        #creating a movemenet flag: start with a ship thats not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ships position based on the movement flag """
        #update the ships x value, not the rect
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed
        


        #update rect oject from self.x
        #this adds only the integer position instead of the more accurate react postion which is fine for displaying purposes 
        self.rect.x= self.center



    def blitme(self):
        """Draw the ship ay its current location """
        self.screen.blit(self.image, self.rect)

'''