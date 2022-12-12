import re

def parse_initial_stack(lines):
    no_of_cols = get_cols_no(lines[0])
    stacks = [[] for _ in range(no_of_cols + 1)]
    for line in lines:
        for i in range(no_of_cols):
            el = get_ith_column(line, i)
            if el != ' ':
                stacks[i+1].insert(0, el)
    return stacks

def get_ith_column(line, i):
    return line[1 + 4*i]

def get_cols_no(line):
    return (len(line) + 2) // 4

mode = 'SINGLE'
with open('data.txt') as f:
    initial_setup = []
    while f:
        line = f.readline()
        if line == '\n':
            break
        else:
            initial_setup.append(line[:-1])
    stacks = parse_initial_stack(initial_setup[:-1])

    while f:
        line = f.readline()
        if line:
            quantity, source, dest  = map(lambda x: int(x), re.search(r"move ([0-9]*) from ([0-9]*) to ([0-9]*)", line).groups())
            if mode == 'SINGLE':
                for i in range(quantity):
                    el = stacks[source].pop()
                    stacks[dest].append(el)
            else: 
                el = stacks[source][-quantity:]
                stacks[source] = stacks[source][:-quantity]
                stacks[dest] = stacks[dest] + el
        else:
            break
    print(''.join([el[-1] for el in stacks[1:]]))
