from obstacle import Obstacle
from runner import Runner
class Controller:
    def __init__(self):
        '''
        initializes the controller object
        '''
        import pygame
    def mainloop(self):
        '''
        the main loop for the controller
        '''
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            "detect collisions/updates"
            "redraw next frame"
            pygame.display.flip()