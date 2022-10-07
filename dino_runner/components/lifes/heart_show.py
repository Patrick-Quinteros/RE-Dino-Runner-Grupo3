from dino_runner.components.lifes.life import LifeAdd
import random


class Live(LifeAdd):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 150