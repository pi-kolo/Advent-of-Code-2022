def priority(letter):
    if ord(letter) <= 90:
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def get_priorities_of_misplaced(data):
    return sum([priority(letter) if letter in set(word[int(len(word)/2):]) else 0 for word in data for letter in set(word[:int(len(word)/2)])])

def get_common(A, B, C):
    return (set(A) & set(B) & set(C)).pop()

def get_groups_priorities(data):
    elves = [line.strip() for line in data]
    return sum([priority(get_common(elves[i], elves[i+1], elves[i+2])) for i in range(0, len(elves), 3)])

with open('data.txt') as f:
    print(get_priorities_of_misplaced(f.readlines()))

with open('data.txt') as f:
    print(get_groups_priorities(f.readlines()))


