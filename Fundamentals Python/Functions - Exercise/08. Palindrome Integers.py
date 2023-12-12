def is_palindrome(number):
    for num in number:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
is_palindrome(numbers)