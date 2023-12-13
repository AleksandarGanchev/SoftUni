groceries = input().split('!')

command = input()
while command != 'Go Shopping!' :
    command_args = command.split()
    if command_args[0] == 'Urgent':
        urgent_item = command_args[1]
        if not urgent_item in groceries:
            groceries.insert(0, urgent_item)

    elif command_args[0] == 'Unnecessary':
        unnecessary_item = command_args[1]
        if unnecessary_item in groceries:
            groceries.remove(unnecessary_item)

    elif command_args[0] == 'Correct':
        old_item = command_args[1]
        new_item = command_args[2]
        if old_item in groceries:
            groceries = [new_item if item == old_item else item for item in groceries]

    elif command_args[0] == 'Rearrange':
        rearrange_item = command_args[1]
        if rearrange_item in groceries:
            groceries.remove(rearrange_item)
            groceries.append(rearrange_item)


    command = input()

print(*groceries,sep=', ')
