from code import interact
from pickle import FALSE
import pygame
from dino_runner.components.obstacleabove.bird import Bird
from dino_runner.components.obstacleabove.obstacleabove import ObstacleAbove
from dino_runner.utils.constants import BIRD


class ObstacleManagerAvobe():
    def __init__(self):
        self.obstacles_above = []

    def update(self, game):

        if len(self.obstacles_above) == 0:
            self.obstacles_above.append(Bird(BIRD))
            

        for object_above in self.obstacles_above:
            object_above.update(game.game_speed, self.obstacles_above)
            if game.player.dino_rect.colliderect(object_above.rect):
                pygame.time.delay(500)
                
                if not game.player.shield:
                    

                    self.obstacles_above = []
                    game.player_heart_manager.reduce_heart()

                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        
                        
                        break
                else:
                    self.obstacles_above.remove(object)

    def draw(self, screen):
        for object_above in self.obstacles_above:
          object_above.draw(screen)

    def reset_obstacles_avobe(self):
        self.obstacles_above = []
