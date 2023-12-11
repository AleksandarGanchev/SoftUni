working_day_events = input().split('|')
flag = True
energy = 100
coins = 100
for command in working_day_events:

    event_args = command.split('-')
    event = event_args[0]
    number = int(event_args[1])

    if event == 'rest':
        if energy + number >= 100:
            print(f"You gained {abs(100 - energy)} energy.")
            energy = 100
            print('Current energy: 100.')

        else:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")

    if event == 'order':
        if energy - 30 >= 0:
           energy -= 30
           coins += number
           print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")


    elif event != 'rest' and event != 'order':
            if coins >= number:
                coins -= number
                print(f"You bought {event}.")
            else:
                print(f"Closed! Cannot afford {event}." )
                flag = False
                break


if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")