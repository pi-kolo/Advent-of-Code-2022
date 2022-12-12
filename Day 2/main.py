class RockPaperScissor:
    VALUES = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    POINTS_MAP = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    STRATEGY = {
        'X': {
            'A': ['C', 3],
            'B': ['A', 1],
            'C': ['B', 2]
        },
        'Y': {
            'A': ['A', 1],
            'B': ['B', 2],
            'C': ['C', 3]
        },
        'Z': {
            'A': ['B', 2],
            'B': ['C', 3],
            'C': ['A', 1]
        }
    }

    ROCK = ['A', 'X']
    PAPER = ['B', 'Y']
    SCISSORS = ['C', 'Z']

    def __init__(self, turn):
        self.turn = turn

    def __eq__(self, other):
        return self.turn == other.turn \
            or (self.turn in self.ROCK and other.turn in self.ROCK) \
            or (self.turn in self.PAPER and other.turn in self.PAPER) \
            or (self.turn in self.SCISSORS and other.turn in self.SCISSORS) 
    
    def __gt__(self, other):
        if self.turn in self.ROCK: 
            return other.turn in self.SCISSORS
        elif self.turn in self.PAPER:
            return other.turn in self.ROCK
        else:
            return other.turn in self.PAPER

    def get_points_from_move(self, expected_result):
        return self.STRATEGY[expected_result][self.turn][1]


    def value(self):
        return self.values[self.turn]

def count_rps_result(filename): 
    with open(filename) as f:
        return sum([RockPaperScissor(moves[1]).value() + (6 if RockPaperScissor(moves[1]) > RockPaperScissor(moves[0]) else 3 if RockPaperScissor(moves[1]) == RockPaperScissor(moves[0]) else 0) for moves in [line.split() for line in f.readlines()]])

def count_rps_result_modified(filename):
    with open(filename) as f:
        return sum([RockPaperScissor(moves[0]).get_points_from_move(moves[1]) + RockPaperScissor.POINTS_MAP[moves[1]] for moves in [line.split() for line in f.readlines()]])

print(count_rps_result('data.txt'))
print(count_rps_result_modified('data.txt'))
    