gifts = input().split()
flag = False
new_list = []

while not flag:
    command = input()
    if command == "No Money":
        flag = True
        break

    command_args = command.split()

    if command_args[0] == 'OutOfStock':
        for word in range(len(gifts)):
           if gifts[word] == command_args[1]:
               gifts[word] = 'None'

    elif command_args[0] == 'Required':
        for index in range(len(gifts)):
            if index == int(command_args[2]):
                gifts[index] = command_args[1]


    elif command_args[0] == 'JustInCase':
        gifts[-1] = command_args[1]

for correct_word in gifts:
    if correct_word != 'None':
        print(correct_word,end= ' ')