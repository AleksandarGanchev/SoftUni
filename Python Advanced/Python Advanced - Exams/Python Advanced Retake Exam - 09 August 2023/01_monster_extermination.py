from collections import deque

armour_values = deque(int(x) for x in input().split(","))
soldier_strikes = deque(int(x) for x in input().split(","))

killed_monsters = 0
while armour_values and len(soldier_strikes) > 0:
    first_armour = armour_values.popleft()
    last_strike = soldier_strikes.pop()

    result = last_strike - first_armour

    if result >= 0:
        killed_monsters += 1
        if len(soldier_strikes) > 0 and result > 0:
            soldier_strikes[-1] += result
        else:
            if result > 0:
                soldier_strikes.append(result)

    elif result < 0:
        armour_values.append((abs(result)))


if not armour_values:
    print("All monsters have been killed!")

if not soldier_strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
