import os.path
import random

# import basic pygame modules
import pygame

import classes.View
import classes.Controller

# Sprites.
import classes.sprites.ByteSprite
import classes.sprites.BoltSprite
import classes.sprites.SymbolSprites
import classes.sprites.Kills
import classes.sprites.Font

# Actions.
import classes.actions.Shoot

# Utils.
import classes.util.SoundLoader
import classes.util.ImageLoader
import classes.util.StageLoader

# set the path
main_dir = os.path.split(os.path.abspath(__file__))[0]

# Set up classes.
View = classes.View.View()
Input = classes.Controller.Input()
ByteSprite = classes.sprites.ByteSprite
BoltSprite = classes.sprites.BoltSprite
SymbolSprites = classes.sprites.SymbolSprites
Kills = classes.sprites.Kills
Font = classes.sprites.Font
Shoot = classes.actions.Shoot.Shoot()
SoundLoader = classes.util.SoundLoader.SoundLoader(main_dir)
ImageLoader = classes.util.ImageLoader.ImageLoader(main_dir)
StageLoader = classes.util.StageLoader.StageLoader()
clock = pygame.time.Clock()  # for fps


# see if we can load more than standard BMP
ImageLoader.check_load_image()

# set screen rect
SCREENRECT = pygame.Rect(0, 0, 1280, 720)

# Set up the game.
pygame.init()

# Check for sound.
SoundLoader.check_sound()

# Set display mode.
screen = View.load_view(SCREENRECT.size, 0, 32)

# Init game groups
allSprites = pygame.sprite.RenderUpdates()
bolts = pygame.sprite.Group()
symbols = pygame.sprite.Group()
kills = pygame.sprite.Group()
fonts = pygame.sprite.Group()
byte = pygame.sprite.Group()

# Load images, assign to sprites.
byteSpriteSheet = ImageLoader.load_sprite_sheet((100, 100), 'assets/sprites/Byte.gif', (0, 0))
boltImg = ImageLoader.load_image('assets/sprites/bolt.gif')  # Used later when firing
symbolsSpriteSheet = ImageLoader.load_sprite_sheet((50, 50), 'assets/sprites/symbolsSprites.gif', (0, 0))  # enemies

# Create Byte sprite.
Byte = ByteSprite.ByteSprite(
    [allSprites, byte],  # pass in the groups
    byteSpriteSheet,
    SCREENRECT,  # Rect
    ImageLoader
)

# Decorate the window.
View.decorate_window(Byte.images[1], (32, 32))

# Load sounds in.
boltSound = SoundLoader.load_sound('assets/sounds/boltFire.ogg')
hitSound = SoundLoader.load_sound('assets/sounds/ByteHitSound.ogg')
# Load music in.
song_end = pygame.USEREVENT + 1
SoundLoader.load_music('assets/music/ByteSoundtrack.ogg', song_end)

# Set constants for enemies spawns.
symbol_spawn = 9000
symbol_odds = 200
symbol_image = 0
symbol_speed = 1

# Set the current stage.
stage = 0
background = None

start_load_artwork = 0
load_next_artwork = 165  # time in between loading artwork

# Load in the kill counter.
if pygame.font:
    Kills = Kills.Kills(
        [allSprites, kills],  # groups
        0,  # max kills
        'assets/fonts/freesansbold.ttf',  # font to use for text
        10  # font size
    )

# Load in the intro artwork.
while song_end:
    # Load in the art.
    images = ImageLoader.load_images(
        ['assets/art/startImg1.gif',
         'assets/art/startImg2.gif',
         'assets/art/startImg3.gif',
         'assets/art/startImg4.gif']
    )
    # Check the time between loading artwork
    # and load accordingly.
    View.check_load_intro(
        screen,
        images,
        start_load_artwork,
        load_next_artwork,
        allSprites
    )
    start_load_artwork = start_load_artwork + 1

    stage = Input.get_sys_input(song_end)
    if stage == 1:
        song_end = not song_end
        allSprites.clear(screen, images[3])
        # Set the max kills for level 1.
        Kills.set_max_level_kills(25)
        # Load stage 1.
        background = StageLoader.load_stage(
            View,
            ImageLoader,
            'assets/bg/background.gif',
            SCREENRECT,
            screen,
            'assets/music/ByteSoundtrackLoop.ogg'
        )

# Start the game...
while Byte.alive() and stage != 0:
    # Get input...
    # If user hits Esc or they click X, quit.
    Input.get_sys_input()

    # Load stage 2.
    if Kills.get_kills() == 25 and stage != 2:
        stage = 2
        # Set max level kills for stage 2.
        Kills.set_max_level_kills(75)
        background = StageLoader.load_stage(
            View,
            ImageLoader,
            'assets/bg/background2.gif',
            SCREENRECT,
            screen,
            'assets/music/ByteSoundtrackStage2Loop.ogg'
        )
        # Update enemy constants.
        symbol_spawn = 6000
        symbol_odds = 100
        symbol_speed = 1.5

        # Update player constants.
        Shoot.set_max_shots(4)
        Shoot.set_speed(5)

    # Load stage 3.
    if Kills.get_kills() == 75 and stage != 3:
        stage = 3
        # Set max level kills for stage 3.
        Kills.set_max_level_kills(150)
        background = StageLoader.load_stage(
            View,
            ImageLoader,
            'assets/bg/background3.gif',
            SCREENRECT,
            screen,
            'assets/music/ByteSoundtrackStage3Loop.ogg'
        )
        # Update enemy constants.
        symbol_spawn = 3000
        symbol_odds = 50
        symbol_speed = 2

        # Update player constants.
        Shoot.set_max_shots(5)
        Shoot.set_speed(6)

    # Load outro.
    if Kills.get_kills() == 150:
        stage = None
        # Stop the music.
        pygame.mixer.music.stop()
        # Play the win music.
        SoundLoader.load_music('assets/music/ByteWinMusic.ogg')
        # Display "You Win" text
        if pygame.font:
            Font.Font(
                [allSprites, fonts],  # sprite groups
                'assets/fonts/freesansbold.ttf',  # font
                40,  # font size
                'YOU WIN! YOU PROTECTED THE USER!',  # message
                250,  # position x
                320  # position y
            )
        allSprites.clear(screen, background)
        Byte.kill()

    # Handle player input.
    Input.set_player_input()

    # Clear/erase the last drawn sprites
    allSprites.clear(screen, background)

    # Update all sprites
    allSprites.update()

    # Handle player input
    # Get directions.
    Byte.set_directions(Input)

    # Move the character.
    Byte.move()

    # Check if player is trying to shoot.
    Shoot.shoot(
        Input,  # for player input
        Byte,  # for getting the relative direction to character
        BoltSprite,
        allSprites,  # for groups
        bolts,  # for groups
        boltImg,
        boltSound
    )

    # Spawn in enemies
    symbol_spawn = symbol_spawn - 1
    if symbol_image > 3:
        symbol_image = 0
    elif not int(random.random() * symbol_odds):
        symbol_spawn = 0
        SymbolSprites.SymbolSprites(
            [symbols, allSprites],
            symbolsSpriteSheet[symbol_image],
            SCREENRECT,
            symbol_speed
        )
        symbol_image = symbol_image + 1

    # Check if sprite collision.
    # If so, update kills.
    for symbol in pygame.sprite.groupcollide(bolts, symbols, 1, 1).keys():
        # play a death sound
        hitSound.play()
        # switch to death animation
        Kills.add_kill()

    # Check symbol collision with player.
    for symbol in pygame.sprite.groupcollide(byte, symbols, 1, 1):
        # Stop the music.
        pygame.mixer.music.stop()
        # Play the lose music.
        SoundLoader.load_music('assets/music/ByteLoseMusic.ogg')
        # Play a death sound
        hitSound.play()
        # Display "You Lose" text
        if pygame.font:
            Font.Font(
                [allSprites, fonts],  # sprite groups
                'assets/fonts/freesansbold.ttf',  # font
                40,  # font size
                'YOU LOSE',  # message
                500,  # position x
                320  # position y
            )
        # Remove the sprite.
        Byte.kill()

    # Draw the sprites
    dirty = allSprites.draw(screen)
    pygame.display.update(dirty)

    # cap the framerate
    clock.tick(120)

pygame.time.wait(2000)
