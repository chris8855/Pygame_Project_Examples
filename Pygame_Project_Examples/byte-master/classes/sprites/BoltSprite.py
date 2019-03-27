import math
import pygame


class BoltSprite(pygame.sprite.Sprite):
    def __init__(self, containers, images, mouse_position, position, speed, position_x, position_y):
        self.containers = containers
        pygame.sprite.Sprite.__init__(self, containers)  # create sprite

        # Images & animation
        self.image = images[0]  # set the first image
        self.images = images  # an array of imgs with all sprite imgs

        # Positions
        self.mouse_x, self.mouse_y = mouse_position[0], mouse_position[1]
        self.position = position
        self.speed = speed
        self.rect = self.image.get_rect(midbottom=position)
        self.position_x = position_x
        self.position_y = position_y

    def update(self):
        # Get the direction of the mouse compared to the player.
        distance = [self.mouse_x - self.position_x, self.mouse_y - self.position_y]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1] / norm]
        bullet_vector = [direction[0] * self.speed, direction[1] * self.speed]

        # Set the direction.
        self.rect.x += bullet_vector[0]
        self.rect.y += bullet_vector[1]

        # Remove sprites if they reach end of screen.
        if self.rect.x <= 0 \
                or self.rect.x >= 1280 \
                or self.rect.y <= 0 \
                or self.rect.y >= 720:
            self.kill()
