import pygame
import math
class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self,x, y, img_file = "assets/obstacle.png"):
        super().__init__()
        """
        Initializes the Obstacle object
        args:
        - x : int - starting x coordinate
        - y : int - starting y coordinate
        - img_file : str - path to img file
        """
        self.image = pygame.image.load(img_file)
        self.rect= self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xvel = 0
        self.yvel = 0
        self.time = 0
    def move(self):
        '''
        makes the obstacle move toward the runner
        args: none
        return: none
        '''
        self.rect.x -= self.xvel
    def update(self):
        '''
        updates the obstacle's values
        args: none
        return: none
        '''
        self.time +=1
        self.xvel = 2 + math.sqrt(self.time/100)