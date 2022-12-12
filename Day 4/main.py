def is_subgroup(A, B):
    return A[0] <= B[0] and A[1] >= B[1]

def group_overlaps(A, B):
    return (A[0] <= B[0] and A[1] >= B[0]) or (A[0] >= B[0] and A[0] <= B[1])

with open('data.txt') as f:
    groups = [[[int(pair[0]), int(pair[1])] for pair in map(lambda x: x.split('-'), group)] for group in [line.strip().split(',') for line in f.readlines()]]
    print(sum([is_subgroup(group[0], group[1]) or is_subgroup(group[1], group[0]) for group in groups]))
    print(sum([group_overlaps(group[0], group[1]) for group in groups]))