#settings


class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width=600
        self.screen_height=400
        self.bg_color=(36,36,43) #RBG colour grid - I used a custom dark grey for spacelike background
        
    # Ship settings.
        self.ship_speed = 1.5
    
    # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (160,60,60)
        self.bullets_allowed = 5 


