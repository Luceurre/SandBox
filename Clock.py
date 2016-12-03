import pygame


class Clock:
    def __init__(self, framerate=120):
        """Classe permettant la gestion du temps, framerate étant le nombre d'affichage et d'update par seconde.
        La méthode update permet de connaitre le nombre de seconde écoulé entre deux appels et de réguler pour que ce temps tourne autour du framerate demandé"""
        self.framerate = framerate
        self.current_time = self.last_time = pygame.time.get_ticks()
        self.delta = 0

    def update(self):
        self.current_time = pygame.time.get_ticks()
        self.delta = self.current_time - self.last_time

        if (1000 / self.framerate - self.delta > 0):
            pygame.time.wait(int(1000 / self.framerate - self.delta))

        self.current_time = pygame.time.get_ticks()
        self.delta = self.current_time - self.last_time
        self.last_time = self.current_time

    @property
    def get_fps(self):
        return 10 ** 3 / self.delta
