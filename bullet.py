import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manages bullets fired from the ship."""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and set its position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet position as a float value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Allow bullet to travel up the screen."""
        self.y -= self.speed_factor
        # Update the rect's position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)