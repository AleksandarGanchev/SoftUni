collecting_items = input().split(', ')

command = input()
while command != 'Craft!':
    command_args = command.split(' - ')
    if command_args[0] == 'Collect':
        if not command_args[1] in collecting_items:
            collecting_items.append(command_args[1])

    elif command_args[0] == 'Drop':
        if command_args[1] in collecting_items:
            collecting_items.remove(command_args[1])

    elif command_args[0] == 'Combine Items':
        old_item, new_item = command_args[1].split(':')
        if old_item in collecting_items:
            old_item_index = collecting_items.index(old_item) + 1
            collecting_items.insert(old_item_index,new_item)

    elif command_args[0] == 'Renew':
        if command_args[1] in collecting_items:
            collecting_items.remove(command_args[1])
            collecting_items.append(command_args[1])

    command = input()

print(', '.join(collecting_items))
