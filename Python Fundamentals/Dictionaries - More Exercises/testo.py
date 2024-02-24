dwarfs = {}

while True:
    command = input()
    if command == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    if (dwarf_name, dwarf_hat_color) not in dwarfs:
        dwarfs[(dwarf_name, dwarf_hat_color)] = dwarf_physics
    else:
        dwarfs[(dwarf_name, dwarf_hat_color)] = max(dwarfs[(dwarf_name, dwarf_hat_color)], dwarf_physics)

# Sorting dwarfs by physics in descending order and then by the total count of dwarfs with the same hat color
sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1], -sum(1 for d in dwarfs if d[1] == x[1])))

# Print the sorted dwarfs
for (name, hat_color), physics in sorted_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")