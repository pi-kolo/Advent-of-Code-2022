import re
from functools import reduce

def parse_input(filename):
    monkeys = {}
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        monkey_no = 0
        for i in range(0, len(lines), 7):
            monkeys[monkey_no] = {}
            monkeys[monkey_no]['items'] = [int(item) for item in re.search(r"Starting items: ([0-9, ]*)", lines[i+1]).group(1).split(', ')]
            monkeys[monkey_no]['op'] = eval('lambda old: ' + lines[i+2].split('=')[-1])
            monkeys[monkey_no]['test'] = int(lines[i+3].split('by')[-1])
            monkeys[monkey_no][True] = int(lines[i+4].split('monkey')[-1])
            monkeys[monkey_no][False] = int(lines[i+5].split('monkey')[-1])
            monkeys[monkey_no]['processed'] = 0
            monkey_no += 1
    return monkeys

def parse_input2(filename):
    monkeys = {}
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        monkey_no = 0
        for i in range(0, len(lines), 7):
            monkeys[monkey_no] = {}
            monkeys[monkey_no]['items'] = [int(item) for item in re.search(r"Starting items: ([0-9, ]*)", lines[i+1]).group(1).split(', ')]
            monkeys[monkey_no]['op'] = eval('lambda old: ' + lines[i+2].split('=')[-1])
            monkeys[monkey_no]['test'] = int(lines[i+3].split('by')[-1])
            monkeys[monkey_no][True] = int(lines[i+4].split('monkey')[-1])
            monkeys[monkey_no][False] = int(lines[i+5].split('monkey')[-1])
            monkeys[monkey_no]['processed'] = 0
            monkey_no += 1
        divisors = [monkey['test'] for monkey in monkeys.values()]
        for i in range(len(monkeys)):
            monkeys[i]['items_mods'] = [{divisor: item % divisor for divisor in divisors} for item in monkeys[i]['items']]
    return monkeys

def main2():
    monkeys = parse_input2('data.txt')
    for round in range(10000):
        for monkey in monkeys.values():
            for item in monkey['items_mods']:
                new = {val[0]: monkey['op'](val[1]) % val[0] for val in item.items()}
                to = monkey[new[monkey['test']] == 0]
                monkeys[to]['items_mods'].append(new)
                monkey['processed'] += 1
            monkey['items_mods'] = []
    print(reduce(lambda x,y: x*y, sorted([el['processed'] for el in monkeys.values()])[-2:]))


def main1():
    monkeys = parse_input2('data.txt')
    print(monkeys)
    for round in range(20):
        for monkey in monkeys.values():
            for item in monkey['items']:
                new = monkey['op'](item) // 3
                to = monkey[new % monkey['test'] == 0]
                monkeys[to]['items'].append(new)
                monkey['processed'] += 1
            monkey['items'] = []
    print(reduce(lambda x,y: x*y, sorted([el['processed'] for el in monkeys.values()])[-2:]))

main1()
main2()

