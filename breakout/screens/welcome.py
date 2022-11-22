import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sprites = pygame.sprite.Group()

        #Select Champion Textbox
        self.textbox1 = TextBox(
            (300, 100), "Select a Champion", color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.textbox1.rect.x, self.textbox1.rect.y= 250, 100

        #Ezreal textbox
        self.textbox2 = TextBox(
            (200, 100), "Ezreal", color=(255, 255, 255), bgcolor=(0, 0, 255)
        )
        self.textbox2.rect.x, self.textbox2.rect.y= 50, 400

        #Annie Textbox
        self.textbox3 = TextBox(
            (200, 100), "Annie", color=(255, 255, 255), bgcolor=(255, 0, 0)
        )
        self.textbox3.rect.x, self.textbox3.rect.y= 300, 400

        #Kenne Textbox
        self.textbox4 = TextBox(
            (200, 100), "Kennen", color=(255, 255, 255), bgcolor=(75, 0, 130)
        )
        self.textbox4.rect.x, self.textbox4.rect.y= 550, 400

        self.sprites.add(self.textbox1, self.textbox2, self.textbox3, self.textbox4)
        self.background = Background()

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.image, self.background.rect)
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.pos
            if self.textbox2.rect.collidepoint(mouse):
                print("Clicked Ez")
                self.current_selection = 'Ezreal'
                self.next_screen = "game"
                self.running = False
            if self.textbox3.rect.collidepoint(mouse):
                print("Clicked Annie")
                self.current_selection = 'Annie'
                self.next_screen = "game"
                self.running = False
            if self.textbox4.rect.collidepoint(mouse):
                print("Clicked Kennen")
                self.current_selection = 'Kennen'
                self.next_screen = "game"
                self.running = False          
