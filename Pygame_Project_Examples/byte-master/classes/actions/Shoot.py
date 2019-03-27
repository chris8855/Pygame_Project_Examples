import pygame


class Shoot:
    def __init__(self):
        self.max_shots = 3
        self.speed = 4
        self.reloading = 0

    def shoot(self,
              player_input,
              character_obj,
              sprite_obj,
              global_group,
              shots_group,
              shots_img,
              shoot_sound):
        firing = player_input.get_player_mouse_input()[0]

        if not self.reloading \
                and firing \
                and len(shots_group) < self.max_shots:
            # play the projectile sound
            shoot_sound.play()

            # Create the sprite.
            sprite_obj.BoltSprite(
                [shots_group, global_group],  # pass in the groups
                [shots_img],  # pass in the image
                pygame.mouse.get_pos(),
                character_obj.rect.center,
                self.speed,  # speed
                character_obj.rect.x,
                character_obj.rect.y
            )

        self.reloading = firing

    def set_max_shots(self, max_shots):
        self.max_shots = max_shots

    def set_speed(self, speed):
        self.speed = speed
