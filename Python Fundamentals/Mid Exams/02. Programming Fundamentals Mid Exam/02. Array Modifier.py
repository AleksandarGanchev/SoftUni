elements = [int(x) for x in input().split()]

command = input()
while command != 'end':
    command_args = command.split()
    if command_args[0] == 'swap':
       first_swap_index = int(command_args[1])
       second_swap_index = int(command_args[2])
       elements[first_swap_index], elements[second_swap_index] = elements[second_swap_index] , elements[first_swap_index]

    elif command_args[0] == 'multiply':
        first_multiply_index = int(command_args[1])
        second_multiply_index = int(command_args[2])
        elements[first_multiply_index] = elements[first_multiply_index] * elements[second_multiply_index]

    elif command_args[0] == 'decrease':
        elements = [x - 1 for x in elements]

    command = input()

elements =  [str(x) for x in elements]

result = ', '.join(elements)
print(result)
