import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets, and create game resources"""
    def __init__(self): #background settings for pygame to function
        pygame.init()
        self.clock = pygame.time.Clock() # needed to control the frame rate, pygame allows 1 tick per loop s
        self.screen = pygame.display.set_mode((1200,800)) #creates a display window
        pygame.display.set_caption("Alien Invaders")

        #set the background colour
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for thep game"""
        while True:
            #Watch the keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Make the most recent dran screen visible
            pygame.display.flip()
            self.clock.tick(60) # pygame will do its best to make the loop last for 60seconds
    
    if __name__ == '__main__':
        # Make a game instance, and run the game.
        ai = AlienInvasion()
        ai.run_game()
    