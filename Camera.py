from Rect import Rect


class Camera:
    """Fonction de translation"""
    def __init__(self, width=640, height=480):
        self.rect = Rect(0, 0, width, height)

    def translate(self, rect):
        return rect.move(-self.rect.x, -self.rect.y)
