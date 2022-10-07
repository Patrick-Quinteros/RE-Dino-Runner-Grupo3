import pygame
from dino_runner.components.lifes.heart_show import Live
from dino_runner.components.lifes.life import LifeAdd
from dino_runner.utils.constants import HEART_LIS


class LifeManager():
    def __init__(self):
        self.life = []

    def update(self, game):
        if len(self.life) == 0:
            self.life.append(Live(HEART_LIS))

        for heart in self.life:
          heart.update(game.game_speed, self.life)
          if game.player.dino_rect.colliderect(heart.rect):
              pygame.time.delay(100)

              if not game.player.shield :

                  self.life = []
                  game.player_heart_manager.increment_heart()

        
                  
                


                  # if game.player_heart_manager.heart_count < 4:
                  #     game.player.shield = False

    def draw(self, screen):
        for heart in self.life:
          heart.draw(screen)

    def reset_life(self):
        self.life = []