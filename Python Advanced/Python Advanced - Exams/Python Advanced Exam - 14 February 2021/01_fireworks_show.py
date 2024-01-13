from collections import deque

fireworks_effect = deque(int(x) for x in input().split(", "))
explosive_power = deque(int(x) for x in input().split(", "))

firework_types = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

enough_fireworks = False
while fireworks_effect and explosive_power:
    first_firework = fireworks_effect.popleft()
    if first_firework <= 0:
        continue
    last_explosive = explosive_power.pop()
    if last_explosive <= 0:
        fireworks_effect.appendleft(first_firework)
        continue

    result = first_firework + last_explosive

    if result % 3 == 0 and result % 5 == 0:
        firework_types["Crossette Fireworks"] += 1

    elif result % 3 == 0:
        firework_types["Palm Fireworks"] += 1

    elif result % 5 == 0:
        firework_types["Willow Fireworks"] += 1

    else:
        fireworks_effect.append(first_firework-1)
        explosive_power.append(last_explosive)

    if (
            firework_types["Crossette Fireworks"] >= 3
            and firework_types["Palm Fireworks"] >= 3
            and firework_types["Willow Fireworks"] >= 3
    ):
        enough_fireworks = True
        break

if enough_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks_effect])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for firework_type, amount in firework_types.items():
    print(f"{firework_type}: {amount}")
