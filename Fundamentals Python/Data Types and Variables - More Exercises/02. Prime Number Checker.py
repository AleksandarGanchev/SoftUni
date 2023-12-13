number = int(input())

if number > 1:
    if number == 2 or number == 3:
        print("True")
    elif number % 2 == 0 or number % 3 == 0:
        print("False")
    else:
        print("True")