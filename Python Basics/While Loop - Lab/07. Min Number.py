import sys
min_number = sys.maxsize

while True:
    command = input()
    if command != 'Stop':
        number = int(command)
    if number < min_number:
        min_number = number

    if command == 'Stop':
        break

print(min_number)