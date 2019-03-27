import os.path
import pygame


class SoundLoader:
    def __init__(self, path):
        if not pygame.mixer:
            pass
        self.main_dir = path

    @staticmethod
    def check_sound():
        if pygame.mixer and not pygame.mixer.get_init():
            print('Warning, no sound')
            pygame.mixer = None

    def load_sound(self, file):
        file = os.path.join(self.main_dir, file)
        try:
            sound = pygame.mixer.Sound(file)
            return sound
        except pygame.error:
            print('Warning, unable to load: %s' % file)
        return

    def load_music(self, file, song_end=None):
        music = os.path.join(self.main_dir, file)
        if pygame.mixer:
            if song_end is not None:
                pygame.mixer.music.set_endevent(song_end)
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(0)
