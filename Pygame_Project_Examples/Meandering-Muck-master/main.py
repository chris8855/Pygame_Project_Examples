import pygame
from settings import Settings
from slime import Slime
import game_functions as gf


def run_game():
    # Initialize pygame, settings and create screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Meandering Muck - Level " + str(ai_settings.level))

    # Make a Slime.
    slime = Slime(ai_settings, screen)

    # Start main loop for the game.
    while True:
        if ai_settings.gamedone:
            ai_settings.gamedone = False
            ai_settings.level += 1
            pygame.display.set_caption("Meandering Muck - Level " + str(ai_settings.level))
            ai_settings.loadnewsettings()
            slime = None
            slime = Slime(ai_settings, screen)
        gf.check_events(slime)
        slime.update()
        gf.update_screen(ai_settings, screen, slime)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
