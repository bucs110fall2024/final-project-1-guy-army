import pygame

class Text:
    def __init__(self, font, size, antialias, colour, background, text):
        """
        Initializes the Runner object
        args:
        - font: (str) the font of the text
        - size: (int) the size of the text
        - antialias: (bool) does the text have antialiasing?
        - colour: (str) the color of the text
        - background: (str) the background color of the text object
        - text: (str) the text you want printed
        return: none
        """
        self.font = font
        self.size = size
        self.antialias = antialias
        self.colour = colour
        self.background = background
        self.text = text
        self.texts = pygame.font.SysFont(self.font, self.size)
        self.rendered_text = self.texts.render(self.text, self.antialias, self.colour, self.background)
    
      