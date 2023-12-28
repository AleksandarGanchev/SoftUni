command = input()
total = 0

while command != 'NoMoreMoney':
    current_number = float(command)

    if current_number < 0:
        print("Invalid operation!")
        break
    total += current_number
    print(f'Increase: {current_number:.2f}')

    command = input()

print(f'Total: {total:.2f}')