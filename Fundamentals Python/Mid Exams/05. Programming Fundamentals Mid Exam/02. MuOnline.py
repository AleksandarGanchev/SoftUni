health = 100
bitcoins = 0
flag = True

rooms = input().split('|')
counter = 0
for room in rooms:
    counter += 1
    command, number = [int(x) if x[-1].isdigit() else x for x in room.split()]

    if command == 'potion':
        if health + number >= 100:
            added_health = 100 - health
            print(f"You healed for {added_health} hp.")
            print(f"Current health: {health+added_health} hp.")
            health = 100
        else:

            print(f"You healed for {number} hp.")
            print(f"Current health: {health + number} hp.")
            health += number

    elif command == 'chest':
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        monster = command

        if health - number > 0:
            health -= number
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}." )
            print(f"Best room: {counter}")
            flag = False
            break

if flag:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
