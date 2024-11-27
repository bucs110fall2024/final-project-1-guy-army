import pygame
class Runner(pygame.sprite.Sprite):
    
    def __init__(self,x, y, img_file ="assets/runner.jpg"):
        super().__init__()
        """
        Initializes the Runner object
        args:
        - x : int - starting x coordinate
        - y : int - starting y coordinate
        - img_file : str - path to img file
        """
        self.image = pygame.image.load(img_file)
        self.rect = pygame.Rect(x, y, 100, 215)
        self.rect.x = x 
        self.rect.y = y
        self.xvel = 0
        self.yvel = 0
        self.hp = 1
    def jump(self):
        '''
        makes the runner jump
        args: none
        return: none
        '''
        self.rect.y -= 50
        self.yvel -= 20
    def update(self):
        '''
        updates the runner's values
        args: none
        return: none
        '''
        self.yvel += 0.5
        