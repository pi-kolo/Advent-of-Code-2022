from copy import deepcopy
from functools import cmp_to_key

def compare(leftIn, rightIn):
    left = deepcopy(leftIn)
    right = deepcopy(rightIn)
    if isinstance(left, list) and isinstance(right, list):
        x = None
        while len(left) > 0 and len(right) > 0 and (x := compare(left[0], right[0])) == None:
            left.pop(0)
            right.pop(0)
        else:
            if x != None:
                return x
            elif len(left) == 0 and len(right) > 0:
                return True
            elif len(right) == 0 and len(left) > 0:
                return False
            else:
                return None
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(right, int) and isinstance(left, list):
        return compare(left, [right])


def main():
    with open('data.txt') as f:
        data = [[]]
        while f:
            line = f.readline()
            if line:
                if line == '\n':
                    data.append([])
                else:
                    data[-1].append(eval(line))
            else: 
                break

    # part 1
    print(sum(i + 1 for i, line in enumerate(data) if compare(*line) == True))

    # part 2
    flatten_data = [el for line in data for el in line]
    flatten_data.append([[2]])
    flatten_data.append([[6]])
    for i in range(len(flatten_data)):
        for j in range(0, len(flatten_data) - i - 1):
            if compare(flatten_data[j], flatten_data[j + 1]) == False:
                flatten_data[j], flatten_data[j + 1] = flatten_data[j + 1], flatten_data[j]
    print((flatten_data.index([[2]]) + 1) * (flatten_data.index([[6]]) + 1))


main()