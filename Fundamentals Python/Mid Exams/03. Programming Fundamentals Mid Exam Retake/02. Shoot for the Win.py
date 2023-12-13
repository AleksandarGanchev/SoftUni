numbers = [int(x) for x in input().split()]
len_numbers = len(numbers)

command = input()
while command != 'End':
    index = int(command)
    if not 0 <= index < len_numbers:
        command = input()
        continue

    for i in range(len(numbers)):
        if numbers[i] == -1 or index == i:
            continue

        if numbers[index] < numbers[i]:
                numbers[i] -= numbers[index]

        elif numbers[index] >= numbers[i]:
            numbers[i] += numbers[index]

    numbers[index] = -1


    command = input()

shot_targets = len([x for x in numbers if x == -1])

print(f"Shot targets: {shot_targets} ->", *numbers,sep= ' ')