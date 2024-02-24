command = input()
dictionary = {}
while command != "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    if dwarf_hat_color not in dictionary:
        dictionary[dwarf_hat_color] = {}

    if dwarf_name not in dictionary[dwarf_hat_color]:
        dictionary[dwarf_hat_color][dwarf_name] = 0

    if dwarf_physics > dictionary[dwarf_hat_color][dwarf_name]:
        dictionary[dwarf_hat_color][dwarf_name] = dwarf_physics

    command = input()

result = []
for color, info in dictionary.items():
    for dwarf, points in info.items():
        result.append({
            "by_color": len(dictionary[color]),
            "points": points,
            "dwarf": dwarf,
            "color": color
        })


for data in sorted(result, key=lambda x: (-x["points"], -x["by_color"])):
    print(f"({data['color']}) {data['dwarf']} <-> {data['points']}")


