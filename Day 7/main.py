from collections import defaultdict

current_dir = []
structure = {}

def parse_input_line(line):
    if line[:2] == ['$', 'cd']:
        if line[2] == '..':
            current_dir.pop()
        else:
            current_dir.append(line[2])
    elif line[0].isnumeric():
        final_dir = structure
        for dir in current_dir:
            final_dir = final_dir.setdefault(dir, {})
            if 'value' in final_dir.keys(): 
                final_dir['value'] += int(line[0])
            else:
                final_dir['value'] = int(line[0])


def dict_all_items(d):
    childs = list(d.values())
    items = []
    while len(childs):
        child = childs.pop()
        if isinstance(child, dict):
            childs.extend(child.values())
        else:
            items.append(child)
    return items

with open('data.txt') as f:
    data = [line.strip().split(' ') for line in f.readlines()]
    for line in data:
        parse_input_line(line)
    dirs_sizes = dict_all_items(structure)
    print(sum(el for el in dirs_sizes if el < 100000))
    needed_space = 30000000 - (70000000 - max(dirs_sizes))
    print(min([el for el in dirs_sizes if el > needed_space]))
        