class Point(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.S = False
        self.E = False
        self.visited = False
        self.step = 0
        if value == 'S':
            self.height = 0
            self.S = True
        elif value == 'E':
            self.height = ord('z') - ord('a')
            self.E = True
        else:
            self.height = ord(value) - ord('a')
        
    
    def __repr__(self) -> str:
        return f'({self.x}, {self.y}) - {self.step}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
class Lattice():
    def __init__(self, points):
        self.points = points
    
    def height(self):
        return len(self.points)

    def width(self):
        return len(self.points[0])

    def point(self, x, y):
        return self.points[y][x]

    def __getitem__(self, item):
        return self.points[item[1]][item[0]]

    def get_neighbours(self, point):
        neighbours = [(point.x + 1, point.y), (point.x - 1, point.y), (point.x, point.y + 1), (point.x, point.y - 1)]
        return [self[p[0], p[1]] for p in neighbours if p[0] >= 0 and p[0] < self.width() and p[1] >= 0 and p[1] < self.height() and self[p[0], p[1]].height - point.height <= 1]

    def S(self):
        return [item for line in self.points for item in line if item.S][0]

    def E(self):
        return [item for line in self.points for item in line if item.E][0]

    def reset(self):
        for line in self.points:
            for el in line:
                el.step = 0
                el.visited = 0


    def bfs(self, S):
        Q = [S]
        S.step = 0
        while len(Q) > 0:
            node = Q.pop(0)
            if node.visited == True:
                continue
            node.visited = True
            neighbours = [neighbour for neighbour in self.get_neighbours(node) if neighbour.visited == False]
            for neighbour in neighbours:
                neighbour.step = node.step + 1
                if neighbour.E:
                    result = neighbour.step
                    self.reset()
                    return result
            Q.extend(neighbours)

        self.reset()
        return -1

def main():
    with open('data.txt') as f:
        data = [line.strip() for line in f.readlines()]
        grid = [[Point(x, y, el) for x, el in enumerate(line)] for y, line in enumerate(data)]
        lattice = Lattice(grid)
        # part 1
        print(lattice.bfs(lattice.S()))

        #part 2
        lowest = [el for line in lattice.points for el in line if el.height == 0]
        print(min([el for el in [lattice.bfs(el) for el in lowest] if el > -1]))

main()    