import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button 
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game, create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button,
    play_button = Button(ai_settings, screen, "Play")
    # Instance of game statistics.
    stats = GameStats(ai_settings)
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make an alien
    aliens = Group()

    #Create the alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #Listen for action and act accordingly
    while True:
        # Listen for a 'quit' action
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        #refill screen color
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, 
            play_button)

run_game()