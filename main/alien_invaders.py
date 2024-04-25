
#installed with pip via the terminal into the envornment 
import pygame
import sys

<<<<<<< Updated upstream
#created fileS 
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()

''' older code ---  debugging code with end of chapter save point solution
=======
>>>>>>> Stashed changes
class AlienInvasion:
    """Overall class to manage game assets, and create game resources"""
    def __init__(self): #background settings for pygame to function
        pygame.init()
        self.clock = pygame.time.Clock() # needed to control the frame rate, pygame allows 1 tick per loop 
        self.settings = Settings()

        #creates a display window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invaders!!")

        self.ship= Ship(self)
        
        #set the background colour
        #self.bg_color = (230,230,30) #equal ammounts of red, blue, green produces a grey color
        # below is a replacement for the above so settings is where the color is defined
        #self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for thep game"""
        while True:
            
            # this moves the code that manages events to a sperate methods. this will simplify run_game function
            self._check_events() #function created below
            self.ship.update()
            self._update_screen() #function created below
            self.clock.tick(60) # pygame will do its best to make the loop last for 60seconds
    

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # pressed key 
                self._check_keydown_events(event)    
            elif event.type == pygame.KEYUP: # pressed key 
                self._check_keyup_events(event)
            

    def _check_keydown_events(self,event):    
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            #move ship to the right 
            self.ship.moving_right =True            
        elif event.key == pygame.K_LEFT:
            #move ship to the left 
            self.ship.moving_left =True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):    
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _update_screen(self):
        """Update function"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__': 
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()