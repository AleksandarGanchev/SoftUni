from collections import deque

worms = deque(int(x) for x in input().split())
holes = deque(int(x) for x in input().split())

starting_length = len(worms)
matches = 0
while worms and len(holes) > 0:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
        continue

    worm_value = worm - 3

    if worm_value > 0:
        worms.append(worm_value)


if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if matches == starting_length:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if holes:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
else:
    print("Holes left: none")
