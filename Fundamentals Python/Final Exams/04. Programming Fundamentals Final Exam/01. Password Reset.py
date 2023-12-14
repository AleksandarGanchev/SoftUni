string = input()

new_password = ''
command = input()
while command != 'Done':
    command = command.split(' ')
    if command[0] == 'TakeOdd':
        for index, letter in enumerate(string):
            if index % 2 != 0:
                new_password += letter

        string = new_password
        print(string)

    elif command[0] == 'Cut':
        cut, index, length = command
        index = int(index)
        length = int(length)

        end_range = index+length
        string = string[:index] + string[end_range:]
        removed_string = string[index:end_range]

        print(string)

    elif command[0] == 'Substitute':
        sub, substring, substitute = command
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {string}")