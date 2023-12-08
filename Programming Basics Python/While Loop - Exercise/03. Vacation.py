needed_money = float(input())
balance = float(input())
days = 0
spending_days = 0

while balance < needed_money :
    command = input()
    money = float(input())

    if command == 'save':
        balance += money
        days += 1
        spending_days = 0

    elif command == 'spend':
        days += 1
        spending_days += 1
        balance -= money
        if balance < money:
            balance = 0

        if spending_days == 5:
            print(f"You can't save the money.")
            print(f'{days}')
            break

if balance >= needed_money:
        print(f"You saved the money for {days} days.")