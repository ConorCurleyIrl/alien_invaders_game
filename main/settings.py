#settings
class Settings:
    '''a settings class that can be used with the game'''

    def __init__(self) -> None:
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width=600
        self.screen_height=400
        self.bg_color=(36,36,43) #RBG colour grid

        #ship settings
        self.ship_speed = 1.5
