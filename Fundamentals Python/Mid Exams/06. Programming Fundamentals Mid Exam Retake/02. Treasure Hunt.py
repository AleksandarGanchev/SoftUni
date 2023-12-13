treasure_chest = input().split("|")

items_count = 0
command = input()
while command != "Yohoho!":
    command_args = command.split(' ')

    if command_args[0] == 'Loot':
        items = command_args
        items.pop(0)
        for item in items:
            if not item in treasure_chest:
                treasure_chest.insert(0, item)

    elif command_args[0] == 'Drop':
        drop_index = int(command_args[1])
        if 0 <= drop_index < len(treasure_chest):
            item_to_remove = treasure_chest[drop_index]
            treasure_chest.pop(drop_index)
            treasure_chest.append(item_to_remove)

    elif command_args[0] == 'Steal':
        count = int(command_args[1])
        stolen_items = []
        for index in range(count):
            if treasure_chest:
                stolen_items.insert(0, treasure_chest[-1])
                treasure_chest.pop(-1)
        print(*stolen_items,sep=', ')

    command = input()

if treasure_chest:
    unpack_list = (''.join(treasure_chest))
    print(f"Average treasure gain: {len(unpack_list) / len(treasure_chest):.2f} pirate credits.")

else:
    print(f"Failed treasure hunt.")