with open('data.txt') as f:
    data = [list(map(lambda x: int(x), list(line.strip()))) for line in f.readlines()]
    trees = 0
    for y, line in enumerate(data):
        for x, tree in enumerate(line):
            if y == 0 or x == 0 or x == len(line) - 1 or y == len(data) - 1:
                trees += 1
                continue
            
            # visible from top
            for upper in range(0, y):
                if data[upper][x] >= tree:
                    break
            else:
                trees += 1
                continue

            # visible from right
            for right in range(x+1, len(line)):
                if data[y][right] >= tree:
                    break
            else:
                trees += 1
                continue

            # visible from bottom
            for bottom in range(y+1, len(data)):
                if data[bottom][x] >= tree:
                    break
            else:
                trees += 1
                continue

            # visible from left
            for left in range(0, x):
                if data[y][left] >= tree:
                    break
            else: 
                trees += 1
                continue
    print(trees)

def find_distance_to_higher(sequence):
    for i, el in enumerate(sequence[1:]):
        if el >= sequence[0]:
            return i + 1
    return len(sequence) - 1

with open('data.txt') as f:
    data = [list(map(lambda x: int(x), list(line.strip()))) for line in f.readlines()]
    max_dist = 0
    for y, line in enumerate(data):
        for x, tree in enumerate(line):
            if y == 0 or x == 0 or x == len(line) - 1 or y == len(data) - 1:
                continue
            
            # visible from top
            trees_up = [data[i][x] for i in range(y, -1, -1)]
            trees_right = [data[y][i] for i in range(x, len(line))]
            trees_down = [data[i][x] for i in range(y, len(data))]
            trees_left = [data[y][i] for i in range(x, -1, -1)]

            d1 = find_distance_to_higher(trees_up)
            d2 = find_distance_to_higher(trees_right) 
            d3 = find_distance_to_higher(trees_down)
            d4 = find_distance_to_higher(trees_left)
            dist = d1 * d2 * d3 * d4

            if dist > max_dist:
                max_dist = dist
    print(max_dist)
            

