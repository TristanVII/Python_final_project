import pygame
from pygame.math import Vector2

class Ability(pygame.sprite.Sprite):
    #pos = position of champion
    def __init__(self, pos, ability, size):
        super().__init__()
        self.original_image = pygame.image.load(ability)
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.speed = 9

    def set_target(self, pos):
        self.target = Vector2(pos)

    def update(self):
        try:
            move = self.target - self.pos
            move.normalize_ip()
            move = move * self.speed
            self.rect.center += move
            #how to kill if outside screen
        except AttributeError:
            move = (0, 0) - self.pos