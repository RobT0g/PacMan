from random import randint
import MazeGenerator

class Grid:
    def __init__(self):
        self.generateMaze()

    def generateMaze(self):
        # 0 unreachable.
        # 1-4 single way. 1 to right and the others clockwise.
        # 5-10 two-way. 5 to up-right, 'till 8 clockwise. 9 and 10 for straight horizontal and vertical
        # 11-14 three-way. 11 to up-right-down, clockwise for others.
        # 15 four-way.
        self.gridRoot = MazeGenerator.getAMaze()
        self.setPath()
        self.gridPellets = list(map(lambda x: x[:], self.gridRoot))
        self.gridPellets[15][0] = self.gridPellets[16][0] = self.gridPellets[16][1] = 0
        self.gridPellets[17][1] = 0
        self.gridPellets[19][0] = self.gridPellets[18][0] = self.gridPellets[18][1] = 0

    def setPath(self):
        self.gridPath = [[0 for j in range(19)] for i in range(36)]
        for k1, v1 in enumerate(self.gridRoot):
            for k2, v2 in enumerate(v1):
                self.gridPath[k1][k2] = self.getTileId([k1, k2], v2)
        self.gridPath[0][9] = 7
        self.gridPath[-1][9] = 5

    def getTileId(self, pos, v):
        direcs = [0, 0, 0, 0]

        if pos[0]+1 in range(35):
            direcs[0] = 1 if self.gridRoot[pos[0]+1][pos[1]] == 1 else 0
        if pos[1]+1 in range(19):
            direcs[1] = 1 if self.gridRoot[pos[0]][pos[1]+1] == 1 else 0
        if pos[0]-1 in range(35):
            direcs[2] = 1 if self.gridRoot[pos[0]-1][pos[1]] == 1 else 0
        if pos[1]-1 in range(19):
            direcs[3] = 1 if self.gridRoot[pos[0]][pos[1]-1] == 1 else 0
        if v != 1 or (x := direcs.count(1)) == 0:
            return 0
        elif (x := direcs.count(1)) == 1:
            return direcs.index(1)+1
        elif x == 2:
            if direcs == [1, 0, 0, 1]:
                return 5
            if direcs == [1, 1, 0, 0]:
                return 6
            if direcs == [0, 1, 1, 0]:
                return 7
            if direcs == [0, 0, 1, 1]:
                return 8
            if direcs == [0, 1, 0, 1]:
                return 9
            if direcs == [1, 0, 1, 0]:
                return 10
        elif x == 3:
            return (direcs.index(0)+9 if direcs.index(0) in (2, 3) else direcs.index(0)+13)
        return 15

    def getPelletAtPos(self, pos):
        return self.gridPellets[pos[0]][pos[1]]
    
    def delPellet(self, pos):
        self.gridPellets[pos[0]][pos[1]] = 0

    def getDirections(self, pos):
        val = self.gridPath[pos[0]][pos[1]]
        return [val in [1, 5, 6, 10, 11, 12, 14, 15], val in [2, 6, 7, 9, 11, 12, 13, 15], 
            val in [3, 7, 8, 10, 12, 13, 14, 15], val in [4, 5, 8, 9, 11, 13, 14, 15]]
