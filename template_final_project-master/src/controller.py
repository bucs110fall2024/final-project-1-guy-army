import pygame
import pygame_widgets
import random
from pygame_widgets.button import Button
from src.obstacle import Obstacle
from src.runner import Runner
from src.ground import Ground
class Controller:
    def __init__(self):
        '''
        initializes the controller object
        '''
        pygame.init()
        self.state = "MENU" # set starting gamestate 
        def start_playing():
            self.obstacle.rect.x = self.width
            self.coin.rect.x = self.width
            self.coin.rect.y = random.randrange(0, self.obstacle.rect.y - 100)
            self.state = "GAME"
        self.screen = pygame.display.set_mode() # set display mode
        self.width, self.height = pygame.display.get_window_size() # get width and height of screen
        self.background = pygame.Surface((self.width, self.height)) # set background surface
        self.runner = Runner(self.width/6, (self.height/2)-50, img_file = "assets/runner.jpg") # create runner object
        self.start_button = Button(
            self.screen, 
            self.width/2 - 150, 
            self.height/2 - 100, 
            300, 
            200, 
            isSubWidget= False, 
            text = "Click To Start", 
            fontSize = 20, 
            margin = 5, 
            inactiveColour = "red", 
            hoverColour = "maroon", 
            pressedColor = "neon green", 
            radius = 10, 
            onClick=lambda:start_playing()) # makes button object using pygame widgets
        self.ground_blocks = pygame.sprite.Group() # create ground blocks sprite group
        self.max_ground_blocks = 9 # set number of ground blocks
        interval = self.width/ 7 # set how far apart the ground blocks are
        for i in range(self.max_ground_blocks): # add ground blocks to the sprite group
            new_gb = Ground(interval*(i-1), self.height * 5/7, img_file = "assets/ground.png") # create ground block object
            self.ground_blocks.add(new_gb) # add a new ground block
        self.obstacle = Obstacle(self.width, self.height * 5/7, img_file = "assets/obstacle.png") # create obstacle object at the same height as the ground
        obstacle_dimensions = self.obstacle.image.get_size() # finds the dimensions of the obstacle object
        self.obstacle.rect.y -= obstacle_dimensions[1] # moves the obstacle up by it's height
        self.coin = Obstacle(self.width, random.randrange(0, self.obstacle.rect.y - 100), img_file = "assets/coin.png") # create coin object using the obstacle class because they have the same behavior
    def mainloop(self):
        '''
        the main loop for the controller
        '''
        while self.state == "MENU" or self.state == "GAME":
            while self.state == "MENU":
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                self.background_color = "black" # set background color
                self.background.fill(self.background_color)
                self.screen.blit(self.background, (0, 0))
                pygame_widgets.update(events)
                pygame.display.update()
                
            while self.state == "GAME":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE: 
                            if len(pygame.sprite.spritecollide(self.runner, self.ground_blocks, False )) >0:
                                self.runner.jump()
                "detect collisions/updates"
                self.runner.update()
                self.coin.update()
                self.coin.move()
                self.obstacle.update()
                self.obstacle.move()
                if self.obstacle.rect.x < 0:
                    self.obstacle.rect.x = self.width
                if self.coin.rect.x < 0:
                    self.coin.rect.x = self.width
                    self.coin.rect.y = random.randrange(0, self.obstacle.rect.y - 100)
                if len(pygame.sprite.spritecollide(self.runner, self.ground_blocks, False )) > 0:
                    self.runner.yvel = 0 
                    self.runner.rect.y = ((self.height * 5/7) - 210) # snaps runner to the ground when he touches the ground
                else: 
                    self.runner.rect.y += self.runner.yvel
                if self.runner.rect.colliderect(self.obstacle.rect):
                    self.state = "MENU"
                "redraw next frame"     
                self.background_color = "light blue" # set background color
                self.background.fill(self.background_color)
                self.screen.blit(self.background, (0, 0))
                self.ground_blocks.draw(self.screen)
                self.screen.blit(self.obstacle.image, self.obstacle.rect)
                self.screen.blit(self.coin.image, self.coin.rect)
                self.screen.blit(self.runner.image, self.runner.rect)
                pygame.display.flip()
            