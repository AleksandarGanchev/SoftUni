from collections import deque

bomb_effect = deque(int(x) for x in input().split(", "))
bomb_casings = [int(x) for x in input().split(", ")]

bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

bombs_created = False
while bomb_effect and bomb_casings:
    first_effect = bomb_effect.popleft()
    first_casing = bomb_casings.pop()

    result = first_effect + first_casing

    if result == 40:
        bombs["Datura Bombs"] += 1
    elif result == 60:
        bombs["Cherry Bombs"] += 1
    elif result == 120:
        bombs["Smoke Decoy Bombs"] += 1

    else:
        bomb_effect.appendleft(first_effect)
        bomb_casings.append(first_casing-5)

    if (bombs["Datura Bombs"] >= 3
            and bombs["Cherry Bombs"] >= 3
            and bombs["Smoke Decoy Bombs"] >= 3):
        bombs_created = True
        break

if bombs_created:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for bomb, value in sorted(bombs.items()):
    print(f"{bomb}: {value}")
