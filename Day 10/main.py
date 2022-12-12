cycles = [20, 60, 100, 140, 180, 220]

def main1():
    with open('data.txt') as f:
        register_values = []
        lines = [line.strip().split(' ') for line in f.readlines()]
        cycle = 1
        register = 1
        for line in lines:
            if line[0] == 'noop':
                cycle += 1
                if cycle in cycles:
                    register_values.append(register * cycle)
            else:
                cycle += 1
                if cycle in cycles:
                    register_values.append(register * cycle)
                cycle += 1
                register += int(line[1])
                if cycle in cycles:
                    register_values.append(register * cycle)

        print(sum(register_values))


def main2():
    with open('data.txt') as f:
        lines = [line.strip().split(' ') for line in f.readlines()]
        cycle = 1
        register = 1
        crt_position = 0
        crt_lines = ['']
        for line in lines:
            if line[0] == 'noop':
                cycle += 1
                if abs(crt_position - register) <= 1:
                    crt_lines[-1] += '#'
                else:
                    crt_lines[-1] += '.'
                crt_position += 1
                if crt_position == 40:
                    crt_position = 0
                    crt_lines.append('')
            else:
                cycle += 1
                if abs(crt_position - register) <= 1:
                    crt_lines[-1] += '#'
                else:
                    crt_lines[-1] += '.'
                crt_position += 1

                if crt_position == 40:
                    crt_position = 0
                    crt_lines.append('')

                cycle += 1
                if abs(crt_position - register) <= 1:
                    crt_lines[-1] += '#'
                else:
                    crt_lines[-1] += '.'
                register += int(line[1])
                crt_position += 1
                if crt_position == 40:
                    crt_position = 0
                    crt_lines.append('')

        for line in crt_lines:
            print(line)

main2()