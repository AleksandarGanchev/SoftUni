
def sum_numbers(positive, negative):

    print(negative)
    print(positive)

    if abs(negative) > positive:
        print("The negatives are stronger than the positives")

    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
positive_numbers = sum(int(x) for x in numbers if x > 0)
negative_numbers = sum(int(x) for x in numbers if x < 0)
sum_numbers(positive_numbers, negative_numbers)
