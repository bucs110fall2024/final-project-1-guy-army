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
        self.rect= self.image.get_rect()
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
        NOT YET IMPLENTED
        '''
    def slide(self):
        ''' makes the runner slide
        args: none
        return: none
        NOT YET IMPLENTED
        '''
