import pygame
from src.obstacle import Obstacle
from src.runner import Runner
class Controller:
    def __init__(self):
        '''
        initializes the controller object
        '''
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()
        self.state = "GAME"
        self.runner = Runner(self.width/2, self.height/2, img_file = "assets/runner.jpg")
    def mainloop(self):
        '''
        the main loop for the controller
        '''
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            "detect collisions/updates"
            "redraw next frame"
            pygame.display.flip()