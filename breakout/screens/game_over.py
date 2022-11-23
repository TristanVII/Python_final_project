import pygame
from screens import BaseScreen
from components import TextBox



class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.button1 = TextBox(
            (100, 100), "Again", color=(0, 255, 0), bgcolor=(0, 0, 0)
        )
        self.button2 = TextBox(
            (100, 100), "Quit", color=(255, 0, 0), bgcolor=(0, 0, 0)
        )
        #HOW TO ADD TIME HERE
        self.button3 = TextBox(
            (400, 100), f'SCORE = {self.state["score"]}', color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button4 = TextBox(
            (400, 100), f'Survived = {int(self.state["time_alive"])}s', color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button1.rect.topleft = (200, 100)
        self.button2.rect.topleft = (500, 100)
        self.button3.rect.topleft = (200, 400)
        self.button4.rect.topleft = (200, 500)
        self.sprites.add(self.button1, self.button2, self.button3, self.button4)
        print(self.state)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False
