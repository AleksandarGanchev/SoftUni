from collections import deque

elves_energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())

toys = 0
used_energy = 0
counter = 0
while elves_energy and materials:
    curr_elf = elves_energy.popleft()
    if curr_elf < 5:
        continue

    curr_material = materials.pop()
    counter += 1

    if curr_elf < curr_material:
        curr_elf *= 2
        elves_energy.append(curr_elf)
        materials.append(curr_material)
        continue

    if counter % 3 == 0 and counter % 5 == 0:
        if curr_elf >= curr_material * 2:
            used_energy += curr_material * 2
            elves_energy.append(curr_elf - curr_material * 2)
        else:
            elves_energy.append(curr_elf*2)

    elif counter % 3 == 0:
        if curr_elf >= curr_material * 2:
            used_energy += curr_material * 2
            curr_elf -= curr_material * 2
            elves_energy.append(curr_elf+1)
            toys += 2
        else:
            materials.append(curr_material)
            elves_energy.append(curr_elf*2)

    elif counter % 5 == 0:
        if curr_elf >= curr_material:
            curr_elf -= curr_material
            used_energy += curr_material
            elves_energy.append(curr_elf)
        else:
            elves_energy.append(curr_elf*2)

    else:
        if curr_elf >= curr_material:
            used_energy += curr_material
            curr_elf -= curr_material
            elves_energy.append(curr_elf+1)
            toys += 1

print(f"Toys: {toys}")
print(f"Energy: {used_energy}")
if elves_energy:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")
