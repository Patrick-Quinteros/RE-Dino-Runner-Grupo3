from msilib.schema import Class
from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite
import random

class LifeAdd(Sprite):

    def __init__(self, image, type):
      self.image = image
      self.rect = self.image[self.type].get_rect()
      self.type = type
      self.rect.x = SCREEN_WIDTH + random.randint(4000, 5000)
      

    def update(self, game_speed, lifes):
        self.rect.x = self.rect.x - game_speed

        if (self.rect.x < - self.rect.width):
            lifes.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)