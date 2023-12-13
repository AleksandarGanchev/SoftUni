numbers = [int(x) for x in input().split()]

command = input()
while command != 'End':
    command_args = command.split()
    action = command_args[0]
    index = int(command_args[1])
    if action == 'Shoot':
        power = int(command_args[2])
        if 0 <= index < len(numbers):
            numbers[index] -= power
            if numbers[index] <= 0:
                numbers.pop(index)

    elif action == 'Add':
        value = int(command_args[2])
        if 0 <= index < len(numbers):
            numbers.insert(index, value)
        else:
            print("Invalid placement!")

    elif command_args[0] == 'Strike':
        radius = int(command_args[2])
        if 0 <= index-radius < len(numbers) and 0 <= index+radius < len(numbers):
            lower_range = index - radius
            higher_range = index + radius
            for index in range(lower_range, higher_range+1):
                numbers.pop(lower_range)
        else:
            print("Strike missed!")


    command = input()


print(*numbers, sep="|")