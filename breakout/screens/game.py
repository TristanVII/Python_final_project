import random, os
import pygame
from screens import BaseScreen

from components import TextBox
from ..components import Background, Champion, Ability, Enemy

pygame.mixer.init()

class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #champion Selection
        self.current_selection = self.state['current_selection']
        self.champion_selection = {
            "Ezreal": ["./images/ezreal.png", (50, 50), "./images/ezability.png", (20, 15), './sounds/abilitysound.mp3', './sounds/ezdeath.mp3'],
            "Annie": ["./images/annie.png", (60, 60), "./images/fireball.png", (30, 20), './sounds/firesound.mp3', './sounds/anniedeath.mp3'],
            "Kennen": ["./images/kennen.png", (60, 60), "./images/shuriken.png", (40, 40), './sounds/shurikenthrow.mp3', './sounds/kennendeath.mp3']
        }

        #background
        self.background = Background()

        #Champion
        self.champion = Champion(self.champion_selection[self.current_selection][0], self.champion_selection[self.current_selection][1], self.champion_selection[self.current_selection][5])

        #Enemies
        self.enemies = pygame.sprite.Group()

        #Abilities cast
        self.abilities = pygame.sprite.Group()

        #Time & Score
        self.score = 0
        self.time_alive = 0
    
        #Death Screen
        self.death = False
        self.death_boxes = pygame.sprite.Group()
        self.death_box = TextBox(
            (400, 100), f'TEEMO KILLED YOU', color=(0, 0, 0), bgcolor=(255, 0, 0)
        )
        self.death_box.rect.center = (400, 400)
        self.death_boxes.add(self.death_box)

        # Font for scores only in game.oy
        self.font = pygame.font.SysFont('Consolas', 30)

        #Intro tip
        self.tip = self.font.render('Press Q to shoot, RIGHT-CLICK to move', True, (255, 0, 0))

    def update(self):
        self.champion.update()
        self.abilities.update()
        self.enemies.update()
        self.manage_enemies()
        #MANAGE TIME without pygame.time.getticks()
        self.time_alive += 1 / 60
        self.text_time = self.font.render(f'TIME: {str(int(self.time_alive))}s', True, (0, 0, 0))
        self.text_score = self.font.render(f'SCORE:{str(self.score)}', True, (0, 0, 0))

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.image, self.background.rect)
        self.window.blit(self.champion.image, self.champion.rect)
        self.abilities.draw(self.window)
        self.enemies.draw(self.window)
        self.window.blit(self.text_time, (600, 20))
        self.window.blit(self.text_score, (600, 60))
        if self.death != False:
            self.death_boxes.draw(self.window)
        if self.time_alive < 2:
            self.window.blit(self.tip, (70, 200))


    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if (pygame.time.get_ticks() / 1000) - self.champion.cooldown < 0.500:
                    pass
                else:
                    self.champion.cooldown = pygame.time.get_ticks() / 1000
                    print(self.champion.cooldown)
                    ability_direction = pygame.mouse.get_pos()
                    ability = Ability(self.champion.pos, self.champion_selection[self.current_selection][2], self.champion_selection[self.current_selection][3], self.champion_selection[self.current_selection][4])
                    #ability.sound_ability.play()
                    pygame.mixer.music.play(1)
                    ability.set_target(ability_direction)
                    self.abilities.add(ability)
        if event.type == pygame.MOUSEBUTTONDOWN:
            #right click for champion movement
            if event.button == 3:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                self.champion.set_target(mouse_pos)

    def manage_enemies(self):
        if self.time_alive < 30:
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

        if self.time_alive > 30 and self.time_alive < 60:
            if random.randrange(0, 100) < 2:
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

        if self.time_alive > 60:
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
                # self.enemy_death.mixer.music.play()
                pygame.mixer.music.load('./sounds/enemydeathsound.mp3')
                pygame.mixer.music.play(1)
                i.kill()
                self.score += 1
                
        if pygame.sprite.spritecollide(self.champion, self.enemies, dokill=False):
            pygame.mixer.music.load(self.champion.champion_death)
            pygame.mixer.music.play(1)
            self.death = True
            self.draw()
            pygame.display.flip()
            pygame.event.pump()
            #wait 5 seconds before changing screens
            pygame.time.delay(5000)
            self.state["time_alive"] = self.time_alive
            self.next_screen = "game_over"
            self.running = False
            self.state["score"] = self.score
