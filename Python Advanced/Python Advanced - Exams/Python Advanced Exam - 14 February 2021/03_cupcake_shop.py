def stock_availability(inventory_list, *args):

    if args[0] == "delivery":
        for item in args[1:]:
            inventory_list.append(item)

    elif args[0] == "sell" and len(args) == 1:
        inventory_list.pop(0)

    elif str(args[1]).isdigit():
        for _ in range(args[1]):
            inventory_list.pop(0)

    else:
        for item in args[1:]:
            if item in inventory_list:
                while item in inventory_list:
                    inventory_list.remove(item)

    return inventory_list

