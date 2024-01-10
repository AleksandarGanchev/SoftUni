def multiplication_sign(first_number, second_number, third_number):
    if first_number == 0 or second_number == 0 or third_number == 0:
        return "zero"

    counter = 0
    if first_number < 0:
        counter += 1

    if second_number < 0:
        counter += 1

    if third_number < 0:
        counter += 1

    if counter == 1 or counter == 3:
        return "negative"

    else:
        return "positive"


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication_sign(first_number, second_number, third_number))
