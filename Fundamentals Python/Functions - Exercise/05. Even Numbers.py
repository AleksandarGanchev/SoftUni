def is_even(num):
    result = num % 2 == 0
    return result

num = [int(x) for x in input().split()]

print(list(filter(is_even, num)))