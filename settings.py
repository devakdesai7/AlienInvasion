class Settings:
    """A class to store and modify the game's settings"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (31, 40, 45)

        #Ship settings
        self.ship_speed = 1.0
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)    
        self.bullets_allowed = 10

        #Alien settings 
        self.alien_speed = 1.0
        #self.fleet_drop_speed is the fleet's speed of coming down the screen when one of the aliens in the fleet touches any of the edges in horizontal motion
        self.fleet_drop_speed = 8
        #self.fleet_direction represents the fleet's direction where fleet_direction = 1 shows that the fleet is moving right and fleet_direction = -1 shows that the fleet is moving left
        self.fleet_direction = 1

