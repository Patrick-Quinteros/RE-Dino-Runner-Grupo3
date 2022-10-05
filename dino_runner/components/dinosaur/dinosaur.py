import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING
from pygame.sprite import Sprite


class Dinosaur(Sprite):
    x_pos = 80
    y_pos = 310
    y_pos_duck = 340
    jump_level = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.jump_speed = self.jump_level

        self.step_index = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()

        if user_input[pygame.K_DOWN] and self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True

        if not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index <= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index = self.step_index + 1

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index = self.step_index + 1

    def jump(self):
        self.image = JUMPING

        if(self.dino_jump):
            self.dino_rect.y = self.dino_rect.y - (self.jump_speed * 4)
            self.jump_speed = self.jump_speed - 1

        if(self.jump_speed < -self.jump_level):
            self.dino_rect.y = self.y_pos
            self.dino_jump = False
            self.jump_speed = self.jump_level 


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


