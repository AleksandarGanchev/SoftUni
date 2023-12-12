def numbers_to_list():
    new_list = []
    numbers = [float(x)for x in input().split(' ')]

    for number in numbers:
        current_number = round((number))
        new_list.append(current_number)

    print(new_list)

numbers_to_list()