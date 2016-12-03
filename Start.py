import pygame

from GameRegister import GameRegister
from StageSample import StageSample

pygame.init()

fen = pygame.display.set_mode((640, 480))

gr = GameRegister()
gr.register("sprite", pygame.image.load("perso.png").convert(), 0)

menu = StageSample(fen)

while 1:
    menu.act().draw()
    pygame.display.set_caption(str(menu.clock.get_fps))
