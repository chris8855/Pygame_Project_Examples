import random
import pygame


class SymbolSprites(pygame.sprite.Sprite):
    def __init__(self, containers, image, rect, speed):
        self.containers = containers
        pygame.sprite.Sprite.__init__(self, containers)

        # Set sprite image.
        self.image = image

        # Set positions and directions.
        self.screen_rect = rect
        self.rect = self.image.get_rect()
        self.speed = speed
        self.direction_x = random.choice((-1, 1) * 1)
        self.direction_y = random.choice((-1, 1) * 1)
        if self.direction_x < 0:
            self.rect.right = rect.right
        if self.direction_y < 0:
            self.rect.right = rect.right

    def update(self):
        self.rect.move_ip(self.direction_x * self.speed, self.direction_y * self.speed)
        if not self.screen_rect.contains(self.rect):
            # If the sprite moves off the screen left or right.
            if self.rect.x < (self.screen_rect.left + self.rect.width) \
                    or self.rect.x > (self.screen_rect.right - self.rect.width):
                self.direction_x = -self.direction_x
                self.direction_y = -self.direction_y

            # If the sprite moves off the screen top or bottom.
            if self.rect.y < (self.screen_rect.bottom + self.rect.height) \
                    or self.rect.y > (self.screen_rect.top - self.rect.height):
                self.direction_y = -self.direction_y

            self.rect = self.rect.clamp(self.screen_rect)
