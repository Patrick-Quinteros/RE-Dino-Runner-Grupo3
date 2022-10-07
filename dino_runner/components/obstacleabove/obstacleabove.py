from msilib.schema import Class

from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite
import random


class ObstacleAbove(Sprite) :
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(2000,4000)

    def update(self, game_speed,  above):
        self.rect.x = self.rect.x - game_speed

        if(self.rect.x < - self.rect.width):
            above.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)