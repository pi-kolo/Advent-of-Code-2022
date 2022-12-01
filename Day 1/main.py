def get_calories_for_elf(filename):
    calories_for_elf = []
    with open(filename) as f:
        calories = 0
        for line in f.readlines():
            if line == '\n':
                calories_for_elf.append(calories)
                calories = 0
                continue
            calories += int(line)
    return calories_for_elf

# part 1
calories_per_elf = get_calories_for_elf('data.txt')
max_calories = max(calories_per_elf)
print(max_calories)

#part 2
top_three_sum = sum(sorted(calories_per_elf)[-3:])
print(top_three_sum)