import sys
import pygame


class Input:
    def __init__(self):
        self.keyState = None
        self.mouseClickState = None

    @staticmethod
    def get_sys_input(song_end=None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            if event.type == song_end:
                stage = 1
                return stage

    def set_player_input(self):
        self.keyState = pygame.key.get_pressed()
        self.mouseClickState = pygame.mouse.get_pressed()

    def get_player_key_input(self):
        return self.keyState

    def get_player_mouse_input(self):
        return self.mouseClickState

