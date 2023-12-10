number = int(input())
all_even = True

for even in range(number):
    num = int(input())
    if num % 2 == 1:
        print(f'{num} is odd!')
        all_even = False
        break

if all_even:
    print('All numbers are even.')