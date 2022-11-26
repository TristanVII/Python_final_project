import pygame
from screens import BaseScreen
from components import TextBox, InputBox
from web.models import User, Userlist
from web.app import app
import webbrowser


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Flask web app
        self.app = app

        #Check if username is submitted
        self.submit = False

        #Sprites
        self.sprites = pygame.sprite.Group()
        self.button1 = TextBox(
            (100, 100), "Again", color=(0, 255, 0), bgcolor=(255, 255, 255)
        )
        self.button2 = TextBox(
            (100, 100), "Quit", color=(255, 0, 0), bgcolor=(255, 255, 255)
        )
        #HOW TO ADD TIME HERE
        self.button3 = TextBox(
            (400, 100), f'SCORE = {self.state["score"]}', color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.button4 = TextBox(
            (400, 100), f'Survived = {int(self.state["time_alive"])}s', color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.button5 = TextBox(
            (200, 100), 'Username', color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button6 = TextBox(
            (200, 100), 'Enter To Save', color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button7 = TextBox(
            (400, 200), 'VIEW LEADERBOARD', color=(0, 0, 0), bgcolor=(255, 255, 255)
        )

        self.button1.rect.topleft = (200, 100)
        self.button2.rect.topleft = (500, 100)
        self.button3.rect.topleft = (200, 300)
        self.button4.rect.topleft = (200, 400)
        self.button5.rect.topleft = (200, 500)
        self.button6.rect.topleft = (400, 550)
        self.button7.rect.topleft = (200, 500)
        self.sprites.add(self.button1, self.button2, self.button3, self.button4, self.button5, self.button6)

        #TextBox 
        self.input_box = InputBox(400, 525, 600, 50, '')

    
    def update(self):
        self.input_box.update()
        self.get_user()
        if self.submit == True:
            self.sprites.add(self.button7)

    def draw(self):
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)
        if self.submit == False:
            self.input_box.draw(self.window)
        

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False
            if self.button7.rect.collidepoint(event.pos):
                if self.submit == True:
                    self.running = False
                    webbrowser.open_new('http://127.0.0.1:5000')
                    self.app.run()
        #Manage input box event
        self.input_box.handle_event(event)

    def get_user(self):
        if self.input_box.entered != '':
            self.state["username"] = self.input_box.entered
            username = self.state["username"]
            score = self.state['score']
            time = int(self.state["time_alive"])
            user = User(username, score, time)
            users = Userlist()
            users.add(user)
            users.save()
            self.submit = True
