import pygame,random
from settings import *
from sprites import *

class Map:
    def __init__(self, game, width, height):
        self.game = game
        self.width = width
        self.height = height
        # map surface
        self.image = pygame.Surface((width,height))
        # map bg color
        self.image.fill(SPACE)
        self.rect = self.image.get_rect()

        # gen objects
        self.gen_stars()
        self.gen_planets()

    def gen_stars(self):
        # generate stars on map surface
        for numstar in range(int(self.width * self.width * 0.0001)):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            self.image.set_at((x,y), STAR)

    def gen_planets(self):
        # for this game because there is only one map and three object just put everything here, but not recommend for complex map such as tilemap
            sun = Planet(self.game, self.game.sun_img, self.width/2, self.height/2, 3, 500, 500)
            earth = Planet_orbit(self.game, self.game.earth_img, -10, 200, 200, sun, 0.1, 700, 150)
            moon = Planet_orbit(self.game, self.game.moon_img, 36, 50, 50, earth, 1, 150, 150)
