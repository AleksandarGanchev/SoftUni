import sys
max_number = -sys.maxsize

while True:
    command = input()
    if command != 'Stop':
        number = int(command)
    if number > max_number:
        max_number = number

    if command == 'Stop':
        break

print(max_number)