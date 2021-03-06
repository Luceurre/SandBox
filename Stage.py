import pygame

from Clock import Clock


class Stage:
    """Chaque scène a ses propres acteurs, actions et fonctions. Par exemple, le menu et l'écran de jeu seront deux scènes diffèrentes"""

    stages = []
    ids = 0

    def __init__(self, screen):

        self.actors = []
        self.screen = screen
        self.camera = None

        self.clock = Clock()

        self.id = Stage.ids
        Stage.stages.append(self)
        Stage.ids += 1

    def add_actor(self, actor):
        actor.screen = self.screen
        self.actors.append(actor)

    def remove_actor(self, actor_id):
        i = 0
        for actor in self.actors:
            if(actor.id == actor_id):
                print()
                self.actors.pop(i)
            i += 1

    def set_framerate(self, framerate):
        self.clock.framerate = framerate

    def act(self, delta = None):
        """Tout affichage doit se faire dans act"""
        self.clock.update()
        delta = self.clock.delta

        self.screen.fill((0, 0, 0))

        events = pygame.event.get()

        self.actors = sorted(self.actors, key=lambda actor: actor.z)

        i = 0
        for event in events:
            if (self.event_handler(event)):
                pass
            else:
                for actor in self.actors:
                    if (actor.event_handler(event)):
                        pass

        for actor in self.actors:
            if(actor.active):
                actor.update(delta)

        return self

    def draw(self):
        for actor in self.actors:
            if (actor.drawable):
                actor.draw(camera=self.camera)

        pygame.display.flip()

    # Gestion des évènements

    def event_handler(self, event):
        """Renvoie True si l'Actor gère l'évènement, False si elle le gère mais veut le laisser dans la pile ou ne le gère pas"""
        return False
