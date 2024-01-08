from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted_toys = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}


while materials and len(magic_levels) > 0:
    material = materials[-1]
    magic_level = magic_levels[0]

    if material == 0 or magic_level == 0:
        if material == 0:
            materials.pop()
        if magic_level == 0:
            magic_levels.popleft()
        continue

    product = material * magic_level

    if presents.get(product):
        crafted_toys.append(presents[product])
        materials.pop()
        magic_levels.popleft()

    elif product < 0:
        materials.pop()
        magic_levels.popleft()
        materials.append(material+magic_level)

    elif product > 0:
        materials.pop()
        magic_levels.popleft()
        materials.append(material+15)


if {"Doll", "Wooden train"}.issubset(crafted_toys) or {"Teddy bear", "Bicycle"}.issubset(crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
elif magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")


[print(f"{toy}: {crafted_toys.count(toy)}")for toy in sorted(set(crafted_toys))]
