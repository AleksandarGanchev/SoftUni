def numbers_searching(*args):
    min_number = min(args)
    max_number = max(args)

    missing_number = None
    for number in range(min_number, max_number + 1):
        if number not in args:
            missing_number = number
            break

    duplicates = []
    uniques = []
    for num in args:
        if num in uniques and num not in duplicates:
            duplicates.append(num)
        else:
            uniques.append(num)

    return [missing_number, sorted(duplicates)]
