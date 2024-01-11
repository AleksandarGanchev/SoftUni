from collections import deque

caffeine_amounts = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))

consumed_caffeine = 0
while caffeine_amounts and energy_drinks:
    caffeine_mg = caffeine_amounts.pop()
    energy_drink = energy_drinks.popleft()

    caffeine_dose = caffeine_mg * energy_drink

    if consumed_caffeine + caffeine_dose <= 300:
        consumed_caffeine += caffeine_dose
    else:
        energy_drinks.append(energy_drink)
        if consumed_caffeine - 30 > 0:
            consumed_caffeine -= 30
        else:
            consumed_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {consumed_caffeine} mg caffeine.")
