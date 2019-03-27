import pygame


class Font(pygame.sprite.Sprite):
    def __init__(self, containers, font, font_size, message, position_x, position_y):
        self.containers = containers
        pygame.sprite.Sprite.__init__(self, containers)

        self.font = pygame.font.Font(font, font_size)
        self.color = pygame.Color('white')

        self.msg = message
        self.image = self.font.render(self.msg, 0, self.color)

        self.rect = self.image.get_rect().move(position_x, position_y)
