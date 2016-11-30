import pygame

class Rect(pygame.Rect):
    def get_size(self):
        return (self.width, self.height)

    def move_by(self, x, y):
        self.move_ip(x, y)
