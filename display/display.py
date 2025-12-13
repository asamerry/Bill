import pygame, sys
import numpy as np
from utils import *

class Eye:
    def __init__(self, left, width, top, height, color=(39, 213, 155)):
        self.rect = pygame.Rect(left, top, width, height)
        self.color = color 

    def draw(self, screen, top_lid_prop=0, bot_lid_prop=0):
        pygame.draw.ellipse(screen, self.color, self.rect)

        top_lid_state = top_lid_prop * self.rect.height / 2
        bot_lid_state = bot_lid_prop * self.rect.height / 2
        self.top_lid = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, top_lid_state)
        self.bot_lid = pygame.Rect(self.rect.left, self.rect.top + self.rect.height - bot_lid_state + 1, self.rect.width, bot_lid_state)
        
        pygame.draw.rect(screen, (0, 0, 0), self.top_lid)
        pygame.draw.rect(screen, (0, 0, 0), self.bot_lid)

class Animation:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen_width, self.screen_height = get_screen_dimensions()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.left_eye = Eye(0.25 * self.screen_width, 0.15 * self.screen_width, 0.25 * self.screen_height, 0.5 * self.screen_height)
        self.right_eye = Eye(0.6 * self.screen_width, 0.15 * self.screen_width, 0.25 * self.screen_height, 0.5 * self.screen_height)
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    # take_input()
                    pass

        pygame.display.update()
        self.clock.tick(60)

    def close_eyes(self):
        states = [x**2 for x in np.linspace(0, 1, 30)]
        for state in states:
            self.screen.fill((0, 0, 0))
            self.left_eye.draw(self.screen, state, state)
            self.right_eye.draw(self.screen, state, state)
            self.update()

    def open_eyes(self):
        states = [x**2 for x in np.linspace(1, 0, 30)]
        for state in states:
            self.screen.fill((0, 0, 0))
            self.left_eye.draw(self.screen, state, state)
            self.right_eye.draw(self.screen, state, state)
            self.update()

    def blink(self):
        self.close_eyes()
        for _ in range(15): 
            self.left_eye.draw(self.screen, 1)
            self.right_eye.draw(self.screen, 1)
        self.open_eyes()

    def run(self):
        i = 0
        while True:
            self.screen.fill((0, 0, 0))

            self.left_eye.draw(self.screen)
            self.right_eye.draw(self.screen)

            if i % 600 == 0:
                self.blink()

            self.update()
            i += 1
    
Animation().run()

