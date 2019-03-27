import pygame
import numpy
from numpy.random import randint as rand
import maze as mz


class Settings:
    """A class to store all settings for Meandering Muck"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (54, 38, 32)
        # Slime Settings.
        self.slime_speed_factor = 3
        # Maze Settings
        self.maze_width = 4
        self.maze_height = 4
        self.orig_bg = pygame.image.load("./images/stonefloor.gif")
        self.orig_stone = {}
        self.orig_stone.update({1: pygame.image.load("./images/wall.gif")})
        self.orig_stone.update({11: pygame.image.load("./images/wall3.gif")})
        self.orig_stone.update({27: pygame.image.load("./images/wall2.gif")})
        self.orig_slime = pygame.image.load('./images/slime.gif')
        self.orig_start_img = pygame.image.load("./images/stairsup.gif")
        self.orig_end_img = pygame.image.load("./images/starsdown.gif")
        self.orig_slime.set_colorkey((255, 255, 255))
        self.maze_block_width = None
        self.maze_block_height = None
        self.slime = None
        self.slime_width = None
        self.slime_height = None
        self.maze = None
        self.startx = None
        self.starty = None
        self.bg = None
        self.stone = []
        self.walls = []
        self.start = None
        self.end = None
        self.gamedone = False
        self.level = 1
        self.loadnewsettings()

    def loadnewsettings(self):
        self.maze_width += 2
        self.maze_height += 2
        self.maze_block_width = self.screen_width / self.maze_width
        self.maze_block_height = self.screen_height / self.maze_height
        self.slime_width = self.maze_block_width / 2
        self.slime_height = self.maze_block_height / 2
        self.bg = pygame.transform.flip(self.orig_bg, bool(rand(0, 2)), bool(rand(0, 2)))
        self.stone = {}
        for k,v in self.orig_stone.items():
            self.stone.update({k: pygame.transform.scale(v, (int(self.maze_block_width), int(self.maze_block_height)))})
        self.slime = pygame.transform.scale(self.orig_slime, (int(self.slime_width), int(self.slime_height)))
        self.start_img = pygame.transform.scale(self.orig_start_img, (int(self.maze_block_width), int(self.maze_block_height)))
        self.end_img = pygame.transform.scale(self.orig_end_img, (int(self.maze_block_width), int(self.maze_block_height)))
        self.generatenewmaze()

    def generatenewmaze(self):
        self.maze = mz.make_maze(self)
        for (x, y), value in numpy.ndenumerate(self.maze):
            if value == 2:
                self.startx = x
                self.starty = y
                break
        self.walls, self.start, self.end = mz.define_maze(self, self.maze)
