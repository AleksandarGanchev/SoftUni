activation_key = input()

command = input()
while command != 'Generate':
    command = command.split('>>>')
    if command[0] == 'Contains':
        contains, substring = command
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == 'Flip':
        flip, casetype, start_index, end_index = command
        start_index = int(start_index)
        end_index = int(end_index)
        if casetype == 'Upper':
            changed_casetype = activation_key[start_index:end_index].upper()
            activation_key = activation_key[:start_index] + changed_casetype + activation_key[end_index:]
            print(activation_key)
        elif casetype == 'Lower':
            changed_casetype = activation_key[start_index:end_index].lower()
            activation_key = activation_key[:start_index] + changed_casetype + activation_key[end_index:]
            print(activation_key)

    elif command[0] == 'Slice':
        slice_part,start_index,end_index = command
        start_index = int(start_index)
        end_index = int(end_index)
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")