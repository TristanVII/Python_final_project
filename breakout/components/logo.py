import pygame
class Logo(pygame.sprite.Sprite):
    def __init__(self, image_file, size, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.original_image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location