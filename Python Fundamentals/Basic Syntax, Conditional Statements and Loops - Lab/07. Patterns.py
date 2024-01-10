number = int(input())
counter = 0
second_counter = 0

while counter != number :
    counter += 1
    print('*' * counter)

for i in range(number):
    number -= 1
    print('*' * number)
    if number == 1:
        break