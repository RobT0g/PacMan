import pygame
from GridManager import Grid
from CharacterManager import *

pygame.init()
grid = Grid()
hero = Character()

class Screen:
    def __init__(self, screen) -> None: 
        self.frame = pygame.image.load('Images/Frame.png')
        self.char = [pygame.image.load(f'Images/Pac{i}.png') for i in range(3)] + [
            pygame.image.load(f'Images/Pac1.png')]
        self.bar = [pygame.image.load(f'Images/Barrier{i}.png') for i in range(3)] 
        self.pellet =[pygame.image.load(f'Images/Pellet{i}.png') for i in range(4)]
        self.screen = screen
        self.grid = grid
        self.hero = hero
        self.count = 0
    
    def putOnScreen(self):
        self.screen.blit(self.frame, (0, 0))
        for k1, v1 in enumerate(grid.gridRoot):
            for k2, v2 in enumerate(v1):
                if v2 == 0:
                    self.screen.blit(self.bar[0], self.actualPos([k1, k2]))
                elif v2 == 2:
                    self.screen.blit(self.bar[1], self.actualPos([k1, k2]))
                elif v2 == 4:
                    self.screen.blit(self.bar[2], self.actualPos([k1, k2]))
                if grid.gridPellets[k1][k2] == 1:
                    self.screen.blit(self.pellet[int(self.count/10)], self.actualPos([k1, k2]))
        heroSprite = self.char[int(self.count/8)%4]
        if self.hero.direction != 0:
            heroSprite = pygame.transform.rotate(self.char[int(self.count/8)%4], 360-(
                (self.hero.direction-1)*90))
        self.screen.blit(heroSprite, self.actualPos(self.hero.pos))

    def actualPos(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            return [-32, -32]
        return [(pos[0]*32)+16, (pos[1]*32)+16]

    def update(self):
        self.count = (self.count+1)%4
        self.hero.walk(self.grid)
    
    def setCharDir(self, dir):
        x = grid.getDirections(self.hero.pos)
        if x[dir-1] and dir != 0:
            self.hero.setDirction(dir)

