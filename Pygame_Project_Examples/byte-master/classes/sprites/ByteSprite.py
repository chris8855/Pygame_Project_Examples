import pygame


class ByteSprite(pygame.sprite.Sprite):
    def __init__(self, containers, images, rect, image_loader):
        self.containers = containers  # containers for grouping
        pygame.sprite.Sprite.__init__(self, containers)  # create sprite
        self.ImageLoader = image_loader

        # Images and animation.
        self.animation_counter = 0
        self.index = 0
        self.image = images[0]  # set the first image
        self.images = images  # an array of imgs with all sprite imgs
        self.left_images = images  # same as above, but needs to be static.
        self.right_images = self.ImageLoader.flip_surfaces(images)  # same as above, but flipped.

        # Positions
        self.screen_rect = rect  # the size of the screen
        self.rect = self.image.get_rect(midbottom=rect.midbottom)  # initial placement of sprite
        self.direction_x = None
        self.direction_y = None

    def set_directions(self, keyboard):
        self.direction_x = keyboard.get_player_key_input()[pygame.K_d] - keyboard.get_player_key_input()[pygame.K_a]
        self.direction_y = keyboard.get_player_key_input()[pygame.K_s] - keyboard.get_player_key_input()[pygame.K_w]

    def get_direction_x(self):
        return self.direction_x

    def get_direction_y(self):
        return self.direction_y

    def move(self):
        self.rect.move_ip(self.direction_x * 1, self.direction_y * 1)
        self.rect = self.rect.clamp(self.screen_rect)
        # Change the image & animation depending on what direction.
        if self.direction_x < 0:
            self.image = self.right_images[0]
            self.images = self.right_images
        elif self.direction_x > 0:
            self.image = self.left_images[0]
            self.images = self.left_images

    def update(self):
        # Handle animation.
        self.animation_counter += 1
        if self.animation_counter > 350:  # How long to wait until we play the animation.
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
                self.animation_counter = 0
            self.image = self.images[self.index]
