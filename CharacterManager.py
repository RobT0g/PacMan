class Entity:
    def __init__(self, pos) -> None:
        self.acPos = [(pos[0]*32)+16, (pos[1]*32)+16]
        self.pos = pos
        self.direction = 1
        self.stemDir = [0, 0]


class Character(Entity):
    def __init__(self) -> None:
        super().__init__([17, 1])
        self.points = 0
    
    def incPoint(self, grid):
        if grid.getPelletAtPos(self.pos):
            self.points += 1
            grid.delPellet(self.pos)
        
    def walk(self, grid):
        paths = grid.getDirections(self.pos)
        if paths[self.direction-1] and self.direction != 0:
            if self.direction == 1:
                self.pos[0] = (self.pos[0]+1)%35
            elif self.direction == 2:
                self.pos[1] = (self.pos[1]+1)%19
            elif self.direction == 3:
                self.pos[0] = (self.pos[0]-1)%35
            elif self.direction == 4:
                self.pos[1] = (self.pos[1]-1)%19
        self.incPoint(grid) 
    
    def setDirction(self, dir):
        self.direction = dir

class Enemy(Entity):
    def __init__(self) -> None:
        super().__init__([17, 11])
