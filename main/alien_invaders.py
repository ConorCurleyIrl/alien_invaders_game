import sys

#installed with pip via the terminal into the envornment 
import pygame

#created fileS 
from settings import Settings
from ship import Ship



class AlienInvasion:

    """Overall class to manage game assets, and create game resources"""
    def __init__(self): #background settings for pygame to function
        pygame.init()
        self.clock = pygame.time.Clock() # needed to control the frame rate, pygame allows 1 tick per loop 
        self.settings = Settings()

        #creates a display window
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invaders!!")

        self.ship= Ship(self)
        
        #set the background colour
        self.bg_color = (230,230,230) #equal ammounts of red, blue, green produces a grey color

    def run_game(self):
        """Start the main loop for thep game"""
        while True:
            
            # this moves the code that manages events to a sperate methods. this will simplify run_game function
            self._check_events() #function created below
            self._update_screen() #function created below

            #Watch the keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # redraw the screen during each pass through the loop/
            self.screen.fill(self.bg_color)  
        
            self.ship.blitme() #resetting ship in the bottom center

            #Make the most recent dran screen visible
            pygame.display.flip()
            self.clock.tick(60) # pygame will do its best to make the loop last for 60seconds
    

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                

    def _update_screen(self):
        '''Updates '''

if __name__ == '__main__': #???? i dont know what this means?

    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
        