import pygame
from data import *


class Button(object):  # A GENERAL CLASS FOR ALL THE BUTTONS ON THE SCREEN (LETTERS & LANGUAGE BUTTONS)
    def __init__(self, color, pos, width, height, letter, size=40):
        self.clicked = False
        self.rollOver = False
        self.size = size
        self.font = pygame.font.SysFont(None, self.size)
        self.color = color
        self.letter = letter
        self.pos = pos
        self.width = width
        self.height = height
        self.subsurface = pygame.Surface((self.width, self.height))  # CREATING A SUBSURFACE TO GET A RECT
        self.subsurface.fill(self.color)
        self.text = self.font.render(self.letter, True, colors["white"])

    def draw(self, surface):
        if self.rollOver:  # IF A BUTTON IS UNDER THE MOUSE
            self.subsurface.set_alpha(200)  # MAKE IT LESS VIBRANT
        else:
            self.subsurface.set_alpha(255)

        if not self.clicked:
            surface.blit(self.subsurface, self.pos)
            self.subsurface.blit(self.text, (self.width / 4, self.height / 5))
