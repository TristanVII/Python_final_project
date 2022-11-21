import pygame
from pygame.math import Vector2

class Champion(pygame.sprite.Sprite):
    #pos = position of champion
    def __init__(self, pos=(400, 400)):
        super().__init__()
        self.original_image = pygame.image.load("./images/ezreal.png")
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.speed = 2
        self.cooldown = 0

        # Starting position = middle of the screen, bottom
 
    def set_target(self, pos):
        self.target = Vector2(pos)

    #move with mouse click source: https://stackoverflow.com/questions/16288905/make-a-sprite-move-to-the-mouse-click-position-step-by-step
    def update(self):
        try:
            move = self.target - self.pos
            move_length = move.length()
            if move_length < self.speed:
                self.pos = self.target
            elif move_length != 0:
                move.normalize_ip()
                move = move * self.speed
                self.pos += move
            self.rect.center = list(int(v) for v in self.pos)
        except AttributeError:
            move = (0, 0) - self.pos

