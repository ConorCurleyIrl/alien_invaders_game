#settings


class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width=600
        self.screen_height=400
        self.bg_color=(36,36,43) #RBG colour grid
        
        # Ship settings
        
<<<<<<< Updated upstream
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

=======
        self.ship_speed = 0.25 #reducing the speed from 1.5
    
>>>>>>> Stashed changes

