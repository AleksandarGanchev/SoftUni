wagons = int(input())
wagon_list = [0] * wagons

command = input()
while command != 'End':
    command_args = command.split(' ')
    operation = command_args[0]
    if operation == 'add':
        people = int(command_args[1])
        wagon_list[-1] += people

    elif operation == 'insert':
        wagon_index = int(command_args[1])
        people = int(command_args[2])
        wagon_list[wagon_index] += people

    elif operation == 'leave':
        wagon_index = int(command_args[1])
        people = int(command_args[2])
        wagon_list[wagon_index] -= people

    command = input()

print(wagon_list)