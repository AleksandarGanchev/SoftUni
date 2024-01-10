numbers = [int(x) for x in input().split(', ')]

positive = [number for number in numbers if number >= 0]
negative = [number for number in numbers if number < 0]
even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 != 0]

print(f"Positive: {', '.join([str(x)for x in positive])}")
print(f"Negative: {', '.join([str(x)for x in negative])}")
print(f"Even: {', '.join([str(x)for x in even])}")
print(f"Odd: {', '.join([str(x)for x in odd])}")