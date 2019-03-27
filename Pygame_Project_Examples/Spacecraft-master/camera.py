import pygame
from settings import *

# nothing changed from KidsCanCode's pygame code
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0,0,width,height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)
        # limit scrolling to map size
        x = min(0, x) # left
        y = min(0, y) # up
        x = max(-(self.width - WIDTH), x) # right
        y = max(-(self.height - HEIGHT), y) # down
        self.camera = pygame.Rect(x, y, self.width, self.height)
