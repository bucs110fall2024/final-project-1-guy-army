import pygame
from src.obstacle import Obstacle
from src.runner import Runner
from src.ground import Ground
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
        self.runner = Runner(self.width/4, (self.height/2)-50, img_file = "assets/runner.jpg")
        self.ground = Ground(self.width/4, self.height * 5 / 7, img_file = "assets/ground.png")
        self.ground2 = Ground(0, self.height * 5 / 7, img_file = "assets/ground.png")
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
                        if self.runner.check_collision(self.ground.rect) == True:
                            self.runner.jump()
            "detect collisions/updates"
            "redraw next frame"
            self.runner.yvel += 1
            if self.runner.check_collision(self.ground.rect) == True:
                self.runner.yvel = 0 
            else: 
                self.runner.rect.y += self.runner.yvel
                
                
            self.background.fill(self.background_color)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.ground.image, self.ground.rect)
            self.screen.blit(self.ground2.image, self.ground2.rect)
            self.screen.blit(self.runner.image, self.runner.rect)
            pygame.display.flip()
            