n =int(input())
last_number = 0

for i in range(n):
    number = int(input())
    last_number = number
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    if number != 88 and number != 86 and number < 88:
        print('GREAT!')
    if number > 88:
        print('Bye.')