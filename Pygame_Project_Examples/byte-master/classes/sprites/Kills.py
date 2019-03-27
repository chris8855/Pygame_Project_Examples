import pygame


class Kills(pygame.sprite.Sprite):
    def __init__(self, containers, max_level_kills, font, font_size):
        self.containers = containers
        pygame.sprite.Sprite.__init__(self, containers)

        self.font = pygame.font.Font(font, font_size)
        self.font.set_italic(1)
        self.color = pygame.Color('white')

        self.kills = 0
        self.max_level_kills = max_level_kills
        self.msg = "Texts destroyed: %d / %d" % (self.kills, self.max_level_kills)
        self.image = self.font.render(self.msg, 0, self.color)

        self.rect = self.image.get_rect().move(10, 708)

    def update(self):
        self.msg = "Texts destroyed: %d / %d" % (self.kills, self.max_level_kills)
        self.image = self.font.render(self.msg, 0, self.color)

    def get_kills(self):
        return self.kills

    def add_kill(self):
        self.kills = self.kills + 1

    def set_max_level_kills(self, max_level_kills):
        self.max_level_kills = max_level_kills
