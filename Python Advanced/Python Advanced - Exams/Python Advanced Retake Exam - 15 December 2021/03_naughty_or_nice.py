def naughty_or_nice_list(*args, **kwargs):
    santa_list = args[0]

    output = ""
    nice_list = []
    naughty_list = []
    not_found_list = []

    for command in args[1:]:
        counting_number, behaviour = [int(x) if x.isdigit() else x for x in command.split('-')]

        matching_tuples = [t for t in santa_list if t[0] == counting_number]

        if len(matching_tuples) == 1:
            if behaviour == "Nice":
                nice_list.append(matching_tuples[0][1])
            elif behaviour == "Naughty":
                naughty_list.append(matching_tuples[0][1])

            santa_list.remove(matching_tuples[0])

    for name, action in kwargs.items():
        matching_tuples_two = [t for t in santa_list if t[1] == name]
        if len(matching_tuples_two) == 1:
            if action == "Nice":
                nice_list.append(name)
            elif action == "Naughty":
                naughty_list.append(name)

            santa_list.remove(matching_tuples_two[0])

    if santa_list:
        not_found_list.append([x[1] for x in santa_list])

    if nice_list:
        output += f"Nice: {', '.join([x for x in nice_list])}"'\n'
    if naughty_list:
        output += f"Naughty: {', '.join([x for x in naughty_list])}"'\n'
    if santa_list:
        output += f"Not found: {', '.join([x[1] for x in santa_list])}"

    return output
