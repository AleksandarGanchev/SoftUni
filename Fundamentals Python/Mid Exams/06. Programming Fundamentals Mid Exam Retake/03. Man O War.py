pirate_ship = [int(x)for x in input().split(">")]
war_ship = [int(x)for x in input().split(">")]
health_capacity = int(input())

flag = True
command = input()
while command != 'Retire':
    command_args = command.split()

    if command_args[0] == 'Fire':
        index = int(command_args[1])
        damage = int(command_args[2])
        if 0 <= index <= len(war_ship):
            war_ship[index]-= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                flag = False
                break

    elif command_args[0] == 'Defend':
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        defend_damage = int(command_args[3])

        if 0 <= start_index <= len(pirate_ship) and end_index <= len(pirate_ship):

            for idx in range(start_index,end_index+1):
                pirate_ship[idx] -= defend_damage
                if pirate_ship[idx] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    flag = False
                    break
            if not flag:
                break


    elif command_args[0] == 'Repair':
        repair_index = int(command_args[1])
        repair_health = int(command_args[2])

        if 0 <= repair_index < len(pirate_ship):

            if pirate_ship[repair_index] + repair_health > health_capacity:
                pirate_ship[repair_index] = health_capacity
            else:
                pirate_ship[repair_index] += repair_health


    elif command_args[0] == 'Status':
        max_low_capacity = 0.2 * health_capacity

        capacity_index = 0
        for capacity in pirate_ship:
            if capacity < max_low_capacity:
                capacity_index += 1
        print(f"{capacity_index} sections need repair.")

    command = input()

if flag:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")