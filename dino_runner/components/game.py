import math
import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

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
        pass
        
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.draw_background()
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




            
        
   
            



    # def draw_scroll(self):
    #     self.scroll = 0
    #     image_width = BG.get_width()
    #     bg_rect = BG.get_rect()
    #     tiles = (SCREEN_HEIGHT // image_width) + 1
    #     for i in range(0,tiles):
    #         self.screen.blit(BG,(i  * image_width + self.scroll, 300 )) 
    #         self.y_pos_bg = i * image_width + self.scroll
    #         pygame.draw.rect(self.screen, (255, 255, 255), bg_rect, 1)

    #     self.scroll -= 5

    # def repeat(self):
    #     image_width = BG.get_width()
    #     if abs(self.scroll) > image_width:
    #         self.scroll = 0