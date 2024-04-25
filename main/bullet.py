
import pygame
#this moduke alows you to group related elements in your game and have thme act together 
from pygame.sprite import Group, Sprite

class Bullet(Sprite):
    """a Class to manage bullets fired by the ship"""

    def __init__(self,ai_game):
        """Create a Bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet rect object at (0,0) and then correct position, it does not have an image so this builds it from scratch
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #Store the bullets position as  afloat
        self.y=float(self.rect.y)

    def update(self):
        """ Move the bullet on the screeen """
        #Update the exat position of the bullet
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y=self.y
    
    def draw_bullet(self):
        """Draw the bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)