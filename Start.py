import pygame

from StageSample import StageSample

pygame.init()

fen = pygame.display.set_mode((640, 480))
menu = StageSample(fen)
menu.act().draw()
pygame.time.wait(1500)

while 1:
    delta = pygame.time.get_ticks()
    menu.act().draw()
    pygame.display.set_caption(str(1000 / (pygame.time.get_ticks() - delta + 0.00000000001)))
