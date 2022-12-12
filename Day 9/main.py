

moves = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def are_close(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return True
    return False

def get_new_position(head, tail):
    return (tail[0] + sign(head[0] - tail[0]), tail[1] + sign(head[1] - tail[1]))


def main1():
    H = (0, 0)
    T = (0, 0)
    Ts = set(T)
    with open('data.txt') as f:
        lines = [line.strip().split(' ') for line in f.readlines()]
        for line in lines:
            direction, distance = line
            for _ in range(int(distance)):
                H = (H[0] + moves[direction][0], H[1] + moves[direction][1])
                if are_close(H, T):
                    continue
                else: 
                    T = get_new_position(H, T)
                    Ts.add(T)
        print(len(Ts))

def main2():
    knots = [(0,0) for _ in range(10)]
    Ts = set([(0,0)])
    H = (0,0)
    with open('data.txt') as f:
        lines = [line.strip().split(' ') for line in f.readlines()]
        for line in lines:
            direction, distance = line
            for _ in range(int(distance)):
                H = (H[0] + moves[direction][0], H[1] + moves[direction][1])
                knots[0] = H
                for i, H_i in enumerate(knots[1:], 1):
                    if are_close(H_i, knots[i-1]):
                        continue
                    else: 
                        T = get_new_position(knots[i-1], H_i)
                        knots[i] = T
                        if i == 9:
                            Ts.add(T)
        print(len(Ts))

main1()
main2()