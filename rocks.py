import pygame
pygame.init()

class Rocks:
    def __init__(self, x, y, image):
        width = image.get_width()
        height = image.get_height()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)