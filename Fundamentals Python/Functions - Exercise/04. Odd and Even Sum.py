def even_or_odd(number):
    even_sum = 0
    odd_sum = 0

    for index in number:
        num = int(index)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

command = input()
result = even_or_odd(command)
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")