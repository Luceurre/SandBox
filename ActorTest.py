import Actor
from GameRegister import GameRegister


class ActorTest(Actor.Actor):
    """Juste un jouet"""
    
    def __init__(self):
        super().__init__()
        image = GameRegister().get_sprite(0)
        self.set_image(image)
        self.set_position(5, 5)
        self.velocity = 0.07
        # self.set_scale(0.2, 0.2)

    def update(self, delta):
        if (self.out_of_screen()):
            self.velocity *= -1

        self.rect.move_ip(self.velocity * delta, 0)

    def draw(self, screen=None, camera=None):
        super().draw(screen, camera)



    def event_handler(self, event):
        pass
