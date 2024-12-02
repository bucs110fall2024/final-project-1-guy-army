import pygame
import pygame_widgets
import random
from pygame_widgets.button import Button
from src.obstacle import Obstacle
from src.runner import Runner
from src.ground import Ground
from src.text import Text
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
            self.coin.rect.y = random.randrange(0, self.obstacle.rect.y - 75)
            self.coin_counter.colour = "black"
            self.distance_counter.colour = "black"
            self.max_distance_counter.colour = "black"
            self.obstacle.time = 0
            self.coin.time = 0
            self.state = "GAME"
        def change_coinmult(mult):
            if mult == 2:
                if self.coins >= 20 and self.coinmult_button_2_already_purchased == False:
                    self.coins -= 20
                    self.coin_counter.text = f"coins: {str(self.coins)}"
                    self.coinmult_button_2.setInactiveColour("grey")
                    self.coinmult_button_2.setHoverColour("grey")
                    self.coinmult_button_2.setPressedColour("grey")
                    self.coinmult = self.coinmult * mult
                    self.coinmult_button_2.setText("2x coin multiplyer purchased")
                    self.coinmult_button_2_already_purchased = True
            if mult == 10:
                if self.coins >= 200 and self.coinmult_button_10_already_purchased == False:
                    self.coins -= 200
                    self.coin_counter.text = f"coins: {str(self.coins)}"
                    self.coinmult_button_10.setInactiveColour("grey")
                    self.coinmult_button_10.setHoverColour("grey")
                    self.coinmult_button_10.setPressedColour("grey")
                    self.coinmult = self.coinmult * mult
                    self.coinmult_button_10.setText("10x coin multiplyer purchased")
                    self.coinmult_button_10_already_purchased = True
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
        self.coinmult_button_2 = Button(
            self.screen, 
            self.width/5 - 75, 
            self.height/2 - 100, 
            250, 
            175, 
            isSubWidget= False, 
            text = "Click To Buy 2x Coin Multiplyer (Costs 20 Coins)", 
            fontSize = 10, 
            margin = 20, 
            inactiveColour = "red", 
            hoverColour = "maroon", 
            pressedColor = "neon green", 
            radius = 10, 
            onClick=lambda:change_coinmult(2)) 
        self.coinmult_button_2_already_purchased = False
        self.coinmult_button_10 = Button(
            self.screen, 
            self.width - self.width/5 - 175, 
            self.height/2 - 100, 
            250, 
            175, 
            isSubWidget= False, 
            text = "Click To Buy 10x Coin Multiplyer (Costs 200 Coins)", 
            fontSize = 10, 
            margin = 20, 
            inactiveColour = "red", 
            hoverColour = "maroon", 
            pressedColor = "neon green", 
            radius = 10, 
            onClick=lambda:change_coinmult(10)) 
        self.coinmult_button_10_already_purchased = False
        self.ground_blocks = pygame.sprite.Group() # create ground blocks sprite group
        self.max_ground_blocks = 9 # set number of ground blocks
        interval = self.width/ 7 # set how far apart the ground blocks are
        for i in range(self.max_ground_blocks): # add ground blocks to the sprite group
            new_gb = Ground(interval*(i-1), self.height * 5/7, img_file = "assets/ground.png") # create ground block object
            self.ground_blocks.add(new_gb) # add a new ground block
        self.obstacle = Obstacle(self.width, self.height * 5/7, img_file = "assets/obstacle.png") # create obstacle object at the same height as the ground
        obstacle_dimensions = self.obstacle.image.get_size() # finds the dimensions of the obstacle object
        self.obstacle.rect.y -= obstacle_dimensions[1] # moves the obstacle up by it's height
        self.coin = Obstacle(self.width, random.randrange(0, self.obstacle.rect.y - 75), img_file = "assets/coin.png") # create coin object using the obstacle class because they have the same behavior
        self.coins = 0 # sets coin counter to 0
        self.coin_counter = Text("calibri", 20, True, "white", None, f"coins: {str(self.coins)}")
        self.coinmult = 1
        self.distance = 0 # sets distance counter to 0
        self.distance_counter = Text("calibri", 20, True, "white", None, f"distance: {str(self.distance)}")
        self.max_distance = 0
        self.max_distance_counter = Text("calibri", 20, True, "white", None, f"max distance: {str(self.max_distance)}")
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
                self.screen.blit(
                    self.coin_counter.texts.render(
                        self.coin_counter.text, 
                        self.coin_counter.antialias, 
                        self.coin_counter.colour, 
                        self.coin_counter.background), 
                    (self.width * 13/15, 20)
                    )
                self.screen.blit(
                    self.max_distance_counter.texts.render(
                            self.max_distance_counter.text, 
                            self.max_distance_counter.antialias, 
                            self.max_distance_counter.colour, 
                            self.max_distance_counter.background), 
                        (self.width * 13/15, 50)
                )
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
                    self.distance += 1
                    self.distance_counter.text = f"distance:{str(self.distance)}"
                    if self.distance >= self.max_distance:
                        self.max_distance = self.distance
                        self.max_distance_counter.text = f"max distance:{str(self.max_distance)}"
                    self.obstacle.rect.x = self.width + random.randrange(0, 500) 
                if self.coin.rect.x < 0:
                    self.coin.rect.x = self.width + random.randrange(0, 500)
                    self.coin.rect.y = random.randrange(0, self.obstacle.rect.y - 75)
                if len(pygame.sprite.spritecollide(self.runner, self.ground_blocks, False )) > 0:
                    self.runner.yvel = 0 
                    self.runner.rect.y = ((self.height * 5/7) - 210) # snaps runner to the ground when he touches the ground
                else: 
                    self.runner.rect.y += self.runner.yvel
                if self.runner.rect.colliderect(self.obstacle.rect):
                    self.coin_counter.colour = "white"
                    self.distance_counter.colour = "white"
                    self.max_distance_counter.colour = "white"
                    self.distance = 0
                    self.distance_counter.text = f"distance:{str(self.distance)}"
                    self.state = "MENU"
                if self.runner.rect.colliderect(self.coin.rect):
                    self.coin.rect.x = self.width + random.randrange(0, 500)
                    self.coin.rect.y = random.randrange(0, self.obstacle.rect.y - 75)
                    self.coins += 1 * self.coinmult
                    self.coin_counter.text = f"coins: {str(self.coins)}"
                "redraw next frame"     
                self.background_color = "light blue" # set background color
                self.background.fill(self.background_color)
                self.screen.blit(self.background, (0, 0))
                self.ground_blocks.draw(self.screen)
                self.screen.blit(self.obstacle.image, self.obstacle.rect)
                self.screen.blit(self.coin.image, self.coin.rect)
                self.screen.blit(
                    self.coin_counter.texts.render(
                        self.coin_counter.text, 
                        self.coin_counter.antialias, 
                        self.coin_counter.colour, 
                        self.coin_counter.background), 
                    (self.width * 13/15, 20)
                    )
                self.screen.blit(
                    self.distance_counter.texts.render(
                        self.distance_counter.text, 
                        self.distance_counter.antialias, 
                        self.distance_counter.colour, 
                        self.distance_counter.background), 
                    (self.width * 13/15, 50)
                    )
                self.screen.blit(
                    self.max_distance_counter.texts.render(
                        self.max_distance_counter.text,
                        self.max_distance_counter.antialias,
                        self.max_distance_counter.colour,
                        self.max_distance_counter.background),
                    (self.width * 13/15, 80)
                )
                self.screen.blit(self.runner.image, self.runner.rect)
                pygame.display.flip()
            