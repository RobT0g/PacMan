import pygame
from pygame.locals import *

import ScreenManager

pygame.init()

screen_width = 36*32                                                    # Screen width
screen_height = 20*32                                                   # Screen Height

screen = pygame.display.set_mode((screen_width, screen_height))         # Screen defined
pygame.display.set_caption('pacman')                                    # Screen name

walktime = 300                                                          # 300ms for each half tile walked
clock = pygame.time.Clock()                                             # Internal timer
move_event = pygame.USEREVENT + 1                                       # Move event defined
pygame.time.set_timer(move_event, walktime)                             # New event called each 300ms

sman = ScreenManager.Screen(screen)
sman.putOnScreen()
pygame.display.flip()

running = True                                                          # Flux variable
while running:
    for event in pygame.event.get():
        if event.type == move_event:
            sman.update()
            sman.putOnScreen()
            pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_d]:
            sman.setCharDir(1)
        if pygame.key.get_pressed()[pygame.K_s]:
            sman.setCharDir(2)
        if pygame.key.get_pressed()[pygame.K_a]:
            sman.setCharDir(3)
        if pygame.key.get_pressed()[pygame.K_w]:
            sman.setCharDir(4)
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
        if event.type == QUIT:
            running = False
# Erros:
# Posição ta cagada
