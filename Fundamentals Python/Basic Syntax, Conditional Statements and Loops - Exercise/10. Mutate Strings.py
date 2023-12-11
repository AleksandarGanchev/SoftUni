first_string = input()
second_string = input()

for index in range(len(second_string)):
    if first_string[index] != second_string[index]:
        first_string = second_string[:index + 1] + first_string[index + 1:]
        print(first_string)


