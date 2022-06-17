class GameStats():
    """Track player statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize default statistics that 
        are changed over the course of the game."""
        self.ships_left = self.ai_settings.ship_limit