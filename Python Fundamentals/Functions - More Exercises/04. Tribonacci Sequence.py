def tribonacci_sequence(integer):
    numbers = []
    for index in range(1, integer+1):
        if not len(numbers):
            numbers.append(1)
        elif len(numbers) <= 3:
            number_to_add = sum(numbers)
            numbers.append(number_to_add)
        else:
            number_to_add = sum(numbers[-1:-4:-1])
            numbers.append(number_to_add)
    if numbers:
        numbers = [str(x) for x in numbers]
        numbers = ' '.join(numbers)

    return numbers

number = int(input())
print(tribonacci_sequence(number))
