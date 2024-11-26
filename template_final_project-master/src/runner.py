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
        '''
        self.rect.y -= 50
        self.yvel -= 20
    def check_collision(self, object_rect):
        '''
        checks if the runner is colliding with an object:
        args: 
        - object_rect: Object - the rectangle of the object that the function detects collision with
        return:
        - Bool - True or False 
        '''
        if self.rect.colliderect(object_rect):
            return True
        else:
            return False
