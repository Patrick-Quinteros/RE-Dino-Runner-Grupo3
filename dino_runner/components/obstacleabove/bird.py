from dino_runner.components.obstacleabove.obstacleabove import ObstacleAbove
import random


class Bird(ObstacleAbove):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(150,300)

