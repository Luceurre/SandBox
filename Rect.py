import pygame


class Rect():
    def __init__(self, x=0, y=0, width=0, height=0):
        self.pyrect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_size(self):
        return (self.width, self.height)

    @property
    def size(self):
        return (self.width, self.height)

    def move_ip(self, x, y):
        self.x += x
        self.y += y

    def get_pyrect(self):
        self.pyrect.x = self.x
        self.pyrect.y = self.y
        self.pyrect.width = self.width
        self.pyrect.height = self.height

        return self.pyrect
