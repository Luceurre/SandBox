import math

import pygame

import Rect
from ActorType import ActorType


class Actor:
    """La classe de base de toutes les entités affichées sur l'écran"""

    actors = []
    ids = 0

    def __init__(self):
        self.rect = Rect.Rect((0, 0), (0, 0))
        self.image = None
        self.image_save = None
        self.screen = None
        self.actor_type = ActorType.DEFAULT
        self.rotation = 0
        self.id = Actor.ids
        self.active = True
        self.drawable = True

        Actor.actors.append(self)
        Actor.ids += 1

    def set_width(self, width):
        self.rect.width = width
        self.image = pygame.transform.smoothscale(self.image_save, self.rect.size)

    def set_height(self, height):
        self.rect.height = height
        self.image = pygame.transform.smoothscale(self.image_save, self.rect.size)

    def set_size(self, size):
        self.set_width(size[0])
        self.set_height(size[1])

    def set_scale(self, scale):
        self.set_width(scale * self.rect.width)
        self.set_height(scale * self.rect.height)

    def set_scale(self, scale_x, scale_y):
        self.set_width(scale_x * self.rect.width)
        self.set_height(scale_y * self.rect.height)

    def set_scale_x(self, scale_x):
        self.set_width(scale_x * self.rect.width)

    def set_scale_y(self, scale_y):
        self.set_height(scale_y * self.rect.height)

    def set_rotation(self, angle):
        """Ne pas utiliser ! Encore en développement"""
        self.rotation = angle
        self.rect.size = (math.cos(self.rotation) * self.rect.width, math.sin(self.rotation) * self.rect.height)
        self.image = pygame.transform.rotate(self.image, self.rotation)

    def set_image(self, image):
        self.image = image
        self.image_save = image
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()

    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y

    def set_position(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_rect(self):
        return self.rect

    def move_by(self, x, y):
        self.rect.move_ip(x, y)

    def draw(self, screen=None, camera=None):
        """Methode où l'objet doit être affiché"""

        if (self.screen == None):
            if (screen == None):
                print("[ERROR] Ecran non défini")
            else:
                self.screen = screen

    def update(self, delta):
        """Méthode où l'objet doit être mis à jour, avec delta le temps écoulé"""


    def collide_with(self, actor_type = None):
        actors_collided = []
        for actor in Actor.actors:
            if(actor.id != self.id):
                if(self.rect.colliderect(actor.rect) and (actor_type == None or actor_type == actor.actor_type)):
                    actors_collided.append(actor)

        return actors_collided

    # Gestion des évènements

    def event_handler(self, event):
        """Renvoie True si l'Actor gère l'évènement, False si elle le gère mais veut le laisser dans la pile ou ne le gère pas"""
        return False
