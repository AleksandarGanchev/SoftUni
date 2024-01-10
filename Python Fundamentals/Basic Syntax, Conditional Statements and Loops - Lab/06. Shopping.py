budget = int(input())

command = input()
while command != 'End':
    prices = int(command)
    budget -= prices
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()

if budget >= 0:
    print("You bought everything needed.")