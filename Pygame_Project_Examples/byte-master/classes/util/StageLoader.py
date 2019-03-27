import pygame


class StageLoader:
    @staticmethod
    def load_stage(view, image_loader, file, screen_rect, screen, music_track):
        background = view.load_background(
            image_loader.load_image(file),
            pygame.Surface(screen_rect.size),
            screen_rect,
            screen
        )
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_track)
        pygame.mixer.music.play(-1)
        return background
