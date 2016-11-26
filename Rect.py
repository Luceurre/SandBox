import pygame

class Rect(pygame.Rect):
    def get_size(self):
        return (self.width, self.height)