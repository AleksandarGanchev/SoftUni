dragon_army = {}

for _ in range(int(input())):
    dragon_type, name, damage, health, armor = [int(x) if x.isdigit() else x for x in input().split()]

    if isinstance(damage, str):
        damage = 45
    if isinstance(health, str):
        health = 250
    if isinstance(armor, str):
        armor = 10

    if dragon_type not in dragon_army:
        dragon_army[dragon_type] = {name: [damage, health, armor]}
    else:
        dragon_army[dragon_type][name] = [damage, health, armor]

for drago_color, info in dragon_army.items():

    average_damage = sum([d[0] for d in info.values()]) / len(info)
    average_health = sum([h[1] for h in info.values()]) / len(info)
    average_armor = sum([a[2] for a in info.values()]) / len(info)

    print(f"{drago_color}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for drago_name, values in sorted(info.items()):
        print(f"-{drago_name} -> damage: {values[0]}, health: {values[1]}, armor: {values[2]}")





# dragon_army = {}
#
# for _ in range(int(input())):
#     dragon_type, name, damage, health, armor = [int(x) if x.isdigit() else x for x in input().split()]
#
#     if damage == "null":
#         damage = 45
#     if health == "null":
#         health = 250
#     if armor == "null":
#         armor = 10
#
#     if dragon_type not in dragon_army:
#         dragon_army[dragon_type] = {name: [damage, health, armor]}
#     else:
#         dragon_army[dragon_type][name] = [damage, health, armor]
#
# for drago_color, info in dragon_army.items():
#     average_damage = 0
#     average_health = 0
#     average_armor = 0
#
#     for name, values in info.items():
#         curr_damage, curr_health, curr_armor = values
#         average_damage += curr_damage
#         average_health += curr_health
#         average_armor += curr_armor
#     print(f"{drago_color}::({average_damage/len(info):.2f}/{average_health/len(info):.2f}/{average_armor/len(info):.2f})")
#
#     for drago_name, values in sorted(info.items()):
#         print(f"-{drago_name} -> damage: {values[0]}, health: {values[1]}, armor: {values[2]}")