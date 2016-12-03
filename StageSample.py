import random

import pygame

from ActorTest import ActorTest
from Camera import Camera
from Stage import Stage


class StageSample(Stage):

    def __init__(self, screen):
        super().__init__(screen)

        self.camera = Camera()
        self.camera.rect.x += 0

        for i in range(1000):
            self.add_actor(ActorTest())

        for actor in self.actors:
            actor.rect.x = random.randint(0, self.screen.get_width() - actor.rect.width)
            actor.rect.y = random.randint(0, self.screen.get_height() - actor.rect.height)

        self.actors[0].set_scale(2, 2)
        self.actors[0].z = 50

    def act(self, delta=None):
        super().act()

        # self.camera.rect.x = self.actors[0].rect.x - (self.screen.get_width() - self.actors[0].rect.width) / 2
        # self.camera.rect.y = self.actors[0].rect.y - (self.screen.get_height() - self.actors[0].rect.height) / 2

        return self

    def event_handler(self, event):
        if (event.type == pygame.KEYDOWN):
            self.camera.rect.move_ip(5, 5)
            return True
        else:
            return False
