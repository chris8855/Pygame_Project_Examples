import pygame


class View:
    @staticmethod
    def load_view(size, fullscreen, depth):
        bestdepth = pygame.display.mode_ok(size, fullscreen, depth)
        screen = pygame.display.set_mode(size, fullscreen, bestdepth)
        return screen

    @staticmethod
    def decorate_window(icon_image, size):
        icon = pygame.transform.scale(icon_image, size)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Byte')
        # pygame.mouse.set_visible(0)

    @staticmethod
    def load_background(bg_tile, background, screen_rect, screen):
        for x in range(0, screen_rect.width, bg_tile.get_width()):
            background.blit(bg_tile, (x, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        return background

    @staticmethod
    def check_load_intro(screen, images, start_load_artwork, load_next_artwork, sprite_group):
        if start_load_artwork == 0:
            screen.blit(images[0], (0, 0))
            pygame.display.flip()
        if start_load_artwork == load_next_artwork:
            sprite_group.clear(screen, images[0])
            screen.blit(images[1], (0, 0))
            pygame.display.flip()
        if start_load_artwork == load_next_artwork * 2:
            sprite_group.clear(screen, images[1])
            screen.blit(images[2], (0, 0))
            pygame.display.flip()
        if start_load_artwork == load_next_artwork * 3:
            sprite_group.clear(screen, images[2])
            screen.blit(images[3], (0, 0))
            pygame.display.flip()
