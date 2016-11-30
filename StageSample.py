import pygame

from ActorTest import ActorTest
from Camera import Camera
from Stage import Stage


class StageSample(Stage):

    def __init__(self, screen):
        super().__init__(screen)

        self.camera = Camera()
        self.camera.rect.x += 50

        for i in range(1):
            self.add_actor(ActorTest())

    def event_handler(self, event):
        if (event.type == pygame.KEYDOWN):
            self.camera.rect.move_ip(5, 5)
            return True
        else:
            return False
