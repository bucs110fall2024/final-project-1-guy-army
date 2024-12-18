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
        args: none
        return: none
        '''
        pygame.init()
        self.state = "MENU" 
        def start_playing():
            '''
            switches from the menu screen to the game screen, and does various other housekeeping needed to start playing
            args: none
            return: none
            '''
            self.obstacle.rect.x = self.width
            self.coin.rect.x = self.width
            self.coin.rect.y = random.randrange(0, self.obstacle.rect.y - 75)
            self.coin_counter.colour = "black"
            self.distance_counter.colour = "black"
            self.max_distance_counter.colour = "black"
            self.max_coins_counter.colour = "black"
            self.lives_counter.colour = "black"
            self.obstacle.time = 0
            self.coin.time = 0
            self.runner.lives = self.starting_lives
            self.state = "GAME"
        def change_coinmult(mult):
            '''
            changes the coin multiplier based on which button was pressed
            args:
            - mult : (int) the number by which the coin multiplier should be changed
            return: none
            '''
            if mult == 2:
                if self.coins >= 20 and self.coinmult_button_2_already_purchased == False:
                    self.coins -= 20
                    self.coin_counter.text = f"coins: {str(self.coins)}"
                    self.coinmult_button_2.setInactiveColour("grey")
                    self.coinmult_button_2.setHoverColour("grey")
                    self.coinmult_button_2.setPressedColour("grey")
                    self.coinmult = self.coinmult * mult
                    self.coinmult_button_2.setText("2x coin multiplier purchased")
                    self.coinmult_button_2_already_purchased = True
            if mult == 10:
                if self.coins >= 200 and self.coinmult_button_10_already_purchased == False:
                    self.coins -= 200
                    self.coin_counter.text = f"coins: {str(self.coins)}"
                    self.coinmult_button_10.setInactiveColour("grey")
                    self.coinmult_button_10.setHoverColour("grey")
                    self.coinmult_button_10.setPressedColour("grey")
                    self.coinmult = self.coinmult * mult
                    self.coinmult_button_10.setText("10x coin multiplier purchased")
                    self.coinmult_button_10_already_purchased = True
        def add_starting_life():
            '''
            adds an extra starting life to the runner
            args: none
            return: none
            '''
            if self.coins >= 100:
                self.coins -= 100
                self.coin_counter.text = f"coins: {str(self.coins)}"
                self.starting_lives += 1
                self.lives_counter.text = f"lives: {str(self.starting_lives)}"
        self.screen = pygame.display.set_mode() 
        self.width, self.height = pygame.display.get_window_size() 
        self.background = pygame.Surface((self.width, self.height)) 
        self.runner = Runner(self.width/6, (self.height/2)-50, img_file = "assets/runner.jpg") 
        self.start_button = Button(
            self.screen, 
            self.width/2 - 150, 
            self.height/2 - 300, 
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
            onClick=lambda:start_playing()) 
        self.livesup_button = Button(
            self.screen, 
            self.width/2 - 150, 
            self.height/2 - 50, 
            300, 
            200, 
            isSubWidget= False, 
            text = "Click To Purchase an extra starting life (costs 100 coins)", 
            fontSize = 10, 
            margin = 5, 
            inactiveColour = "red", 
            hoverColour = "maroon", 
            pressedColor = "neon green", 
            radius = 10, 
            onClick=lambda:add_starting_life())
        self.coinmult_button_2 = Button(
            self.screen, 
            self.width/5 - 75, 
            self.height/2 - 100, 
            250, 
            175, 
            isSubWidget= False, 
            text = "Click To Buy 2x Coin Multiplier (Costs 20 Coins)", 
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
            text = "Click To Buy 10x Coin Multiplier (Costs 200 Coins)", 
            fontSize = 10, 
            margin = 20, 
            inactiveColour = "red", 
            hoverColour = "maroon", 
            pressedColor = "neon green", 
            radius = 10, 
            onClick=lambda:change_coinmult(10)) 
        self.coinmult_button_10_already_purchased = False
        self.ground_blocks = pygame.sprite.Group() 
        self.max_ground_blocks = 9
        interval = self.width/ 7 
        for i in range(self.max_ground_blocks): 
            new_gb = Ground(interval*(i-1), self.height * 5/7, img_file = "assets/ground.png") 
            self.ground_blocks.add(new_gb) 
        self.obstacle = Obstacle(self.width, self.height * 5/7, img_file = "assets/obstacle.png") 
        obstacle_dimensions = self.obstacle.image.get_size() 
        self.obstacle.rect.y -= obstacle_dimensions[1]
        self.coin = Obstacle(self.width, random.randrange(0, self.obstacle.rect.y - 75), img_file = "assets/coin.png") 
        self.coins = 0 
        self.coin_counter = Text("calibri", 20, True, "white", None, f"coins: {str(self.coins)}")
        self.coinmult = 1
        self.distance = 0 
        self.distance_counter = Text("calibri", 20, True, "white", None, f"distance: {str(self.distance)}")
        self.max_distance = int((open("assets/distance_high_score.txt", "r")).read())
        self.max_distance_counter = Text("calibri", 20, True, "white", None, f"distance high score: {str((open("assets/distance_high_score.txt", "r")).read())}")
        (open("assets/distance_high_score.txt", "r")).close()
        self.max_coins = int((open("assets/coins_high_score.txt", "r")).read())
        self.max_coins_counter = Text("calibri", 20, True, "white", None, f"coins high score: {str((open("assets/coins_high_score.txt", "r")).read())}")
        (open("assets/coins_high_score.txt", "r")).close()
        self.recentdistance = 0
        self.distance_mult_number = 0
        self.starting_lives = 1
        self.lives_counter = Text("calibri", 20, True, "white", None, f"lives: {str(self.starting_lives)}")
    def mainloop(self):
        '''
        the main loop for the controller
        args: none
        return: none
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
                    (self.width * 10/12, 20)
                    )
                self.screen.blit(
                    self.max_distance_counter.texts.render(
                            self.max_distance_counter.text, 
                            self.max_distance_counter.antialias, 
                            self.max_distance_counter.colour, 
                            self.max_distance_counter.background), 
                        (self.width * 10/12, 50)
                )
                self.screen.blit(
                    self.max_coins_counter.texts.render(
                            self.max_coins_counter.text, 
                            self.max_coins_counter.antialias, 
                            self.max_coins_counter.colour, 
                            self.max_coins_counter.background), 
                        (self.width * 10/12, 80)
                )
                if self.starting_lives > 1:
                    self.screen.blit(
                        self.lives_counter.texts.render(
                                self.lives_counter.text, 
                                self.lives_counter.antialias, 
                                self.lives_counter.colour, 
                                self.lives_counter.background), 
                            (self.width * 1/20, 20)
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
                self.runner.update()
                self.coin.update()
                self.coin.move()
                self.obstacle.update()
                self.obstacle.move()
                if self.obstacle.rect.x < 0:
                    self.distance += 1
                    self.distance_counter.text = f"distance:{str(self.distance)}"
                    if self.distance % 10 == 0 and self.recentdistance != self.distance:
                        self.coinmult *= self.distance/10 + 1
                        self.coinmult /= self.distance/10 
                        self.coinmult = int(self.coinmult)
                        self.recentdistance = self.distance
                        self.distance_mult_number += 1    
                    if self.distance >= self.max_distance:
                        self.max_distance = self.distance
                        distance_hs_file = open("assets/distance_high_score.txt", "w")
                        distance_hs_file.write(str(self.max_distance))
                        distance_hs_file.close
                        distance_hs_file = open("assets/distance_high_score.txt", "r")
                        distance_hs_file_text = distance_hs_file.read()
                        self.max_distance_counter.text = f"distance high score:{str(distance_hs_file_text)}"
                    self.obstacle.rect.x = self.width + random.randrange(0, 500) 
                if self.coin.rect.x < 0:
                    self.coin.rect.x = self.width + random.randrange(0, 500)
                    self.coin.rect.y = random.randrange(0, self.obstacle.rect.y - 75)
                if len(pygame.sprite.spritecollide(self.runner, self.ground_blocks, False )) > 0:
                    self.runner.yvel = 0 
                    self.runner.rect.y = ((self.height * 5/7) - 210) 
                else: 
                    self.runner.rect.y += self.runner.yvel
                if self.runner.rect.colliderect(self.obstacle.rect):
                    self.runner.lives -= 1
                    self.lives_counter.text =  f"lives: {str(self.runner.lives)}"
                    if self.runner.lives == 0:
                        self.coin_counter.colour = "white"
                        self.distance_counter.colour = "white"
                        self.max_distance_counter.colour = "white"
                        self.max_coins_counter.colour = "white"
                        self.lives_counter.colour = "white"
                        self.distance = 0
                        self.distance_counter.text = f"distance:{str(self.distance)}"
                        self.coinmult /= (self.distance_mult_number + 1)
                        self.coinmult = int(self.coinmult)
                        self.distance_mult_number = 0
                        self.runner.lives = self.starting_lives
                        self.lives_counter.text =  f"lives: {str(self.runner.lives)}"
                        self.state = "MENU"
                    else:
                        self.obstacle.rect.x = self.width
                        self.distance += 1
                        self.distance_counter.text = f"distance:{str(self.distance)}"
                        if self.distance >= self.max_distance:
                            self.max_distance = self.distance
                            distance_hs_file = open("assets/distance_high_score.txt", "w")
                            distance_hs_file.write(str(self.max_distance))
                            distance_hs_file.close
                            distance_hs_file = open("assets/distance_high_score.txt", "r")
                            distance_hs_file_text = distance_hs_file.read()
                            self.max_distance_counter.text = f"distance high score:{str(distance_hs_file_text)}"
                if self.runner.rect.colliderect(self.coin.rect):
                    self.coin.rect.x = self.width + random.randrange(0, 500)
                    self.coin.rect.y = random.randrange(0, self.obstacle.rect.y - 75)
                    self.coins += 1 * self.coinmult
                    self.coin_counter.text = f"coins: {str(self.coins)}"
                    if self.coins >= self.max_coins:
                        self.max_coins = self.coins
                        coins_hs_file = open("assets/coins_high_score.txt", "w")
                        coins_hs_file.write(str(self.max_coins))
                        coins_hs_file.close
                        coins_hs_file = open("assets/coins_high_score.txt", "r")
                        coins_hs_file_text = coins_hs_file.read()
                        self.max_coins_counter.text = f"coins high score:{str(coins_hs_file_text)}"
                        coins_hs_file.close()   
                self.background_color = "light blue" 
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
                    (self.width * 10/12, 20)
                    )
                self.screen.blit(
                    self.distance_counter.texts.render(
                        self.distance_counter.text, 
                        self.distance_counter.antialias, 
                        self.distance_counter.colour, 
                        self.distance_counter.background), 
                    (self.width * 10/12, 50)
                    )
                self.screen.blit(
                    self.max_distance_counter.texts.render(
                        self.max_distance_counter.text,
                        self.max_distance_counter.antialias,
                        self.max_distance_counter.colour,
                        self.max_distance_counter.background),
                    (self.width * 10/12, 80)
                )
                self.screen.blit(
                    self.max_coins_counter.texts.render(
                            self.max_coins_counter.text, 
                            self.max_coins_counter.antialias, 
                            self.max_coins_counter.colour, 
                            self.max_coins_counter.background), 
                        (self.width * 10/12, 110)
                )
                if self.starting_lives > 1:
                    self.screen.blit(
                        self.lives_counter.texts.render(
                                self.lives_counter.text, 
                                self.lives_counter.antialias, 
                                self.lives_counter.colour, 
                                self.lives_counter.background), 
                            (self.width * 1/20, 20)
                    )
                self.screen.blit(self.runner.image, self.runner.rect)
                pygame.display.flip()
            