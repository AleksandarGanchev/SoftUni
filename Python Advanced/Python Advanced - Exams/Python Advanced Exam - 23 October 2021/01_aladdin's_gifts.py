from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(int(x) for x in input().split())

presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

f_desired_gifts = {"Gemstone", "Porcelain Sculpture"}
s_desired_gifts = {"Gold", "Diamond Jewellery"}

made_presents = []
while materials and magic_levels:
    curr_material = materials.pop()
    curr_magic = magic_levels.popleft()

    result = curr_material + curr_magic

    if result < 100:
        if result % 2 == 0:
            result = (curr_material * 2) + (curr_magic * 3)
        else:
            result *= 2
            if result < 100:
                continue
    elif result > 499:
        result /= 2

    if 100 <= result <= 199:
        presents["Gemstone"] += 1
        made_presents.append("Gemstone")
    elif 200 <= result <= 299:
        presents["Porcelain Sculpture"] += 1
        made_presents.append("Porcelain Sculpture")
    elif 300 <= result <= 399:
        presents["Gold"] += 1
        made_presents.append("Gold")
    elif 400 <= result <= 499:
        presents["Diamond Jewellery"] += 1
        made_presents.append("Diamond Jewellery")


if f_desired_gifts.issubset(made_presents) or s_desired_gifts.issubset(made_presents):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

if made_presents:
    for present, value in sorted(presents.items()):
        if value:
            print(f"{present}: {value}")
