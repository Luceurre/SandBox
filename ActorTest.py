import pygame

import Actor


class ActorTest(Actor.Actor):
    """Juste un jouet"""
    
    def __init__(self):
        super().__init__()
        image = pygame.image.load("background.jpg").convert()
        self.set_image(image)
        self.set_position(0, 0)

    def draw(self, screen=None, camera=None):
        super().draw(screen)

        rect = self.rect
        if (camera != None):
            rect = camera.translate(rect)

        self.screen.blit(self.image, rect)

    def event_handler(self, event):
        pass
