def operations():
    for index in numbers:
        min_number = min(numbers)
        max_number = max(numbers)
        sum_numbers = sum(numbers)

    print(f"The minimum number is {min_number}",end='\n'), print(f"The maximum number is {max_number}"), print(f"The sum number is: {sum_numbers}")

numbers = [int(x) for x in  input().split()]

(operations())