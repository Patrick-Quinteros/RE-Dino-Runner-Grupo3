import math
import pygame
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.components.obstacles.obstaclesmanager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstaclesmanager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.updates() 
            self.draw()

        pygame.quit()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def updates(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        total_screens = math.ceil((image_width / SCREEN_WIDTH) + 1)
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg) )

        for i in range(0,total_screens):
            self.screen.blit(BG, (i * image_width + self.x_pos_bg, self.y_pos_bg))

        self.x_pos_bg -= self.game_speed

        if abs(self.x_pos_bg) > image_width:
            self.x_pos_bg = 0        



