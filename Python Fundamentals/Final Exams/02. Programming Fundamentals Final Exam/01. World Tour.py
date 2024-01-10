stops = input()

command = input()
while command != 'Travel':
    command = command.split(':')
    if command[0] == 'Add Stop':
        add_stop, index, string = command
        index  = int(index)
        if index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)

    elif command[0] == 'Remove Stop':
        remove_stop, start_index, end_index = command
        start_index = int(start_index)
        end_index = int(end_index)
        if 0 <= start_index and end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]
            # stops = stops - stops[start_index:end_index]
        print(stops)

    elif command[0] == 'Switch':
        switch, old_string, new_string = command
        if old_string in stops:
            stops = stops.replace(old_string,new_string)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")