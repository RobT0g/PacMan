import pygame
pygame.init()

def getOrient():
    if pygame.key.get_pressed()[pygame.K_d]:
        return 1
    if pygame.key.get_pressed()[pygame.K_s]:
        return 2
    if pygame.key.get_pressed()[pygame.K_a]:
        return 3
    if pygame.key.get_pressed()[pygame.K_w]:
        return 4
