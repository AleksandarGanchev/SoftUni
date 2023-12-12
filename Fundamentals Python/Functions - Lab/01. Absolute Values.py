def values():
    new_list = []
    numbers = [float(x)for x in input().split()]
    for number in numbers:
        new_number = abs(number)
        new_list.append(new_number)

    print(new_list)
values()

