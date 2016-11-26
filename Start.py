import pygame

from StageSample import StageSample

pygame.init()

fen = pygame.display.set_mode((640, 480))
menu = StageSample(fen)
menu.act().draw()
pygame.time.wait(1500)

while 1:
    menu.act().draw()
