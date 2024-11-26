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
        self.background_color = "light blue"
        self.runner = Runner(self.width/4, (self.height/2)-50, img_file = "assets/runner.jpg")
        self.ground_blocks = pygame.sprite.Group()
        self.max_ground_blocks = 9
        interval = self.width/ 7
        for i in range(self.max_ground_blocks):
            new_gb = Ground(interval*(i-1), self.height * 5/7, img_file = "assets/ground.png")
            self.ground_blocks.add(new_gb)
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
                        if pygame.sprite.spritecollide(self.runner, self.ground_blocks, False ) == True:
                            self.runner.jump()
            "detect collisions/updates"
            self.runner.update()
            if pygame.sprite.spritecollide(self.runner, self.ground_blocks, False ) == True:
                self.runner.yvel = 0 
            else: 
                self.runner.rect.y += self.runner.yvel
            "redraw next frame"     
            self.background.fill(self.background_color)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.runner.image, self.runner.rect)
            self.ground_blocks.draw(self.screen)
            pygame.display.flip()
            