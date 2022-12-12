with open('data.txt') as f:
    line = f.readline()
    for i in range(14, len(line)):
        if len(set(line[i-14:i])) == 14:
            print(i)
            print(line[:i])
            break