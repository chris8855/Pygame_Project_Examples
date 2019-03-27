import os.path
import pygame


class ImageLoader:
    def __init__(self, path):
        self.main_dir = path

    @staticmethod
    def check_load_image():
        if not pygame.image.get_extended():
            raise SystemExit("Sorry, extended image module required")

    def load_image(self, file):
        file = os.path.join(self.main_dir, file)
        try:
            surface = pygame.image.load(file)
        except pygame.error:
            raise SystemError('Could not load image "%s" %s' % (file, pygame.get_error()))
        return surface.convert()

    def load_images(self, files):
        imgs = []
        for file in files:
            imgs.append(self.load_image(file))
        return imgs

    def load_sprite_sheet(self, size, file, pos=(0, 0)):
        len_sprt_x, len_sprt_y = size  # Sprite size.
        sprt_rect_x, sprt_rect_y = pos  # Location of first sprite on sheet.

        sheet = self.load_image(file).convert_alpha()
        sheet_rect = sheet.get_rect()
        sprites = []
        for i in range(0, sheet_rect.height, size[1]):
            for k in range(0, sheet_rect.width, size[0]):
                sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y))
                sprite = sheet.subsurface(sheet.get_clip())
                sprites.append(sprite)
                sprt_rect_x += len_sprt_x

            sprt_rect_y += len_sprt_y
            sprt_rect_x = 0

        return sprites

    @staticmethod
    def flip_surface(surface):
        return pygame.transform.flip(surface, 1, 0)

    def flip_surfaces(self, surfaces):
        surface_arr = []
        for surface in surfaces:
            surface_arr.append(self.flip_surface(surface))
        return surface_arr
