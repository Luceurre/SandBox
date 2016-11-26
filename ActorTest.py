import Actor
import pygame


class ActorTest(Actor.Actor):
    """Juste un jouet"""
    
    def __init__(self):
        super().__init__()
        image = pygame.image.load("background.jpg").convert()
        self.set_image(image)
        self.set_position(0, 0)

    def draw(self, screen = None, save_screen = True):
        super().draw(screen)
        if(self.screen == None):
            if(screen == None):
                print("[ERROR] Ecran non défini")
            else:
                screen.blit(self.image, self.rect)
                if(save_screen):
                    self.screen = screen
        else:
            self.screen.blit(self.image, self.rect)

    def event_handler(self, event):
        if (event.type == pygame.KEYDOWN):
            self.move_by(5, 5)
            return True
        else:
            return False
