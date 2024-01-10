def factorial_division(f_number, s_number):

    f_factorial = 1
    s_factorial = 1

    for i in range(1, f_number + 1):
        f_factorial = f_factorial * i

    for i in range(1, s_number + 1):
        s_factorial = s_factorial * i

    return f"{f_factorial / s_factorial:.2f}"

first_number = int(input())
second_number = int(input())

print(factorial_division(first_number,second_number))