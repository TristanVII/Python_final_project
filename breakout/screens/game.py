import random
import pygame
from screens import BaseScreen

from components import TextBox
from ..components import Background, Champion, Ability, Enemy


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #background
        self.background = Background()

        #Champion
        self.champion = Champion()

        #Enemies
        self.enemies = pygame.sprite.Group()

        #Abilities cast
        self.abilities = pygame.sprite.Group()

        #Time & Score
        self.score = 0

    def update(self):
        self.champion.update()
        self.abilities.update()
        self.enemies.update()
        #SHOULD THIS BE HERE?
        font = pygame.font.SysFont('Consolas', 30)
        self.text_time = font.render(f'TIME: {str(self.time)}', True, (0, 0, 0))
        self.text_score = font.render(f'SCORE:{str(self.score)}', True, (0, 0, 0))

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.image, self.background.rect)
        self.window.blit(self.champion.image, self.champion.rect)
        self.abilities.draw(self.window)
        self.enemies.draw(self.window)
        self.window.blit(self.text_time, (600, 20))
        self.window.blit(self.text_score, (600, 60))


    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if (pygame.time.get_ticks() / 1000) - self.champion.cooldown < 0.500:
                    pass
                else:
                    self.champion.cooldown = pygame.time.get_ticks() / 1000
                    print(self.champion.cooldown)
                    ability_direction = pygame.mouse.get_pos()
                    ability = Ability(self.champion.pos)
                    ability.set_target(ability_direction)
                    self.abilities.add(ability)
        if event.type == pygame.MOUSEBUTTONDOWN:
            #right click for champion movement
            if event.button == 3:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                self.champion.set_target(mouse_pos)

                

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     self.running = False
        #     self.next_screen = "welcome"

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         self.ball.speed = 10
        #         self.ball.angle = 1.5
    def manage_enemies(self):
        time = int(pygame.time.get_ticks() / 1000)
        if time < 30:
            if random.randrange(0, 100) < 1:
                sides = ['top', 'bottom', 'left', 'right']
                side = random.choice(sides)
                if side == 'top':
                    y = 0
                    x = random.randint(0, 800)
                elif side == 'bottom':
                    y = 800
                    x = random.randint(0, 800)
                elif side == 'left':
                    y = random.randint(0, 800)
                    x = 0
                elif side == 'right':
                    y = random.randint(0, 800)
                    x = 800

                enemy = Enemy((x, y))
                enemy.set_target(self.champion.pos)
                self.enemies.add(enemy)

        if time > 30 and time < 60:
            if random.randrange(0, 100) < 1.5:
                sides = ['top', 'bottom', 'left', 'right']
                side = random.choice(sides)
                if side == 'top':
                    y = 0
                    x = random.randint(0, 800)
                elif side == 'bottom':
                    y = 800
                    x = random.randint(0, 800)
                elif side == 'left':
                    y = random.randint(0, 800)
                    x = 0
                elif side == 'right':
                    y = random.randint(0, 800)
                    x = 800

                enemy = Enemy((x, y))
                enemy.set_target(self.champion.pos)
                self.enemies.add(enemy)

        if time > 60:
            if random.randrange(0, 100) < 3:
                sides = ['top', 'bottom', 'left', 'right']
                side = random.choice(sides)
                if side == 'top':
                    y = 0
                    x = random.randint(0, 800)
                elif side == 'bottom':
                    y = 800
                    x = random.randint(0, 800)
                elif side == 'left':
                    y = random.randint(0, 800)
                    x = 0
                elif side == 'right':
                    y = random.randint(0, 800)
                    x = 800

                enemy = Enemy((x, y))
                enemy.set_target(self.champion.pos)
                self.enemies.add(enemy)
        
        for i in self.enemies:
            i.set_target(self.champion.pos)
            

        for i in self.abilities:
            if pygame.sprite.spritecollide(i, self.enemies, dokill=True):
                i.kill()
                print(self.kill_count)
                self.score += 1
                
        if pygame.sprite.spritecollide(self.champion, self.enemies, dokill=False):
            self.next_screen = "game_over"
            self.running = False
