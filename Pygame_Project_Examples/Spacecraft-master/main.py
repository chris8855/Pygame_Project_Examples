import pygame, sys
from map import *
from camera import *
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        # load assets from assets folders
        game_folder = path.dirname(__file__)
        assets_folder = path.join(game_folder, 'assets')
        # player image
        self.player_img = pygame.image.load(path.join(assets_folder, PLAYER_IMG)).convert_alpha()
        pygame.mixer.music.load(path.join(assets_folder, BG_MUSIC))
        planets_folder = path.join(assets_folder, 'planets')
        # planet images
        self.sun_img = pygame.image.load(path.join(planets_folder, SUN_IMG)).convert_alpha()
        self.earth_img = pygame.image.load(path.join(planets_folder, EARTH_IMG)).convert_alpha()
        self.moon_img = pygame.image.load(path.join(planets_folder, MOON_IMG)).convert_alpha()
        # font
        self.font = pygame.font.Font(None, 30)

    def new(self):
        # one group, map, camera, player
        self.all_sprites = pygame.sprite.Group()
        self.map = Map(self, 2000, 2000)
        self.camera = Camera(self.map.width, self.map.height)
        self.player = Spaceship(self, self.map.width/2, self.map.height/2)
        # start music
        pygame.mixer.music.play(-1)

    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()


    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        #Background
        self.screen.blit(self.map.image, self.camera.apply(self.map))
        #Objects
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #FPS number
        fps = self.font.render(str(int(self.clock.get_fps())), True, pygame.Color('white'))
        self.screen.blit(fps, (50, 50))
        pygame.display.flip()

    def quit(self):
        # stop music
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    while True:
        game.new()
        game.run()
