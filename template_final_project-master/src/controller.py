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
        self.state = "GAME"
        self.width, self.height = pygame.display.get_window_size()
        self.background = pygame.Surface((self.width, self.height))
        self.background_color = "black"
        self.runner = Runner(self.width/2, self.height/2, img_file = "assets/runner.jpg")
    def mainloop(self):
        '''
        the main loop for the controller
        '''
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.runner.rect.y == self.height:
                            self.runner.yvel = 100
                        
            "detect collisions/updates"
            "redraw next frame"
            self.runner.yvel -= 1
            if self.runner.rect.y > self.height:
                self.runner.rect.y += self.runner.yvel
            self.background.fill(self.background_color)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.runner.image, self.runner.rect)
            pygame.display.flip()
            