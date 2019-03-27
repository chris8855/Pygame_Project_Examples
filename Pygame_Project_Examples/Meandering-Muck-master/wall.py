import pygame


class Wall():
    def __init__(self, s, x, y):
        self.rect = pygame.Rect(x, y, s.maze_block_width, s.maze_block_height)
