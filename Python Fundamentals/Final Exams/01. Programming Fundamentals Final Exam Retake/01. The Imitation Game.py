message = input()
new_message = ''
data = input()
while data != 'Decode':
    data = data.split('|')

    if 'Move' in data:
        move_letters = int(data[1])
        message = message[move_letters:] + message[:move_letters]

    elif data[0] == 'Insert':
        index = int(data[1])
        value = data[2]
        message = message[:index] + value + message[index:]

    elif data[0] == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        for _ in message:
            if substring in message:
                message = message.replace(substring,replacement)


    data = input()
print(f"The decrypted message is: {message}")