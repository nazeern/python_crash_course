class Settings():
    def __init__(self):
        # Initialize game settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 3
        self.ship_limit = 3

        # Initialize bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 30
        # 1 represents right, -1 represents left
        self.fleet_direction = 1
