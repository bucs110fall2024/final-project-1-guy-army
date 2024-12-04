import pygame
class Ground(pygame.sprite.Sprite):
    
    def __init__(self,x, y, img_file ="assets/ground.png"):
        super().__init__()
        """
        Initializes the ground object
        args:
        - x : (int) starting x coordinate
        - y : (int) starting y coordinate
        - img_file : (int) path to img file
        return: none
        """
        self.image = pygame.image.load(img_file)
        self.rect=  self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
