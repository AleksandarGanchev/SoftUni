numbers = [ int(x) for x in input().split(', ')]
starting_range = 10

while (len(numbers)) > 0:
    numbers_below = [int(x) for x in numbers if starting_range >= x ]
    numbers = [item for item in numbers if item > starting_range]
    print(f"Group of {starting_range}'s: {numbers_below}")
    starting_range += 10