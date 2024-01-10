n = int(input())
first_set = set()
second_set = set()

longest_intersection = set()
for _ in range(n):
    data = input().split("-")

    first_start, first_end = data[0].split(",")
    first_start, first_end = int(first_start), int(first_end)
    second_start, second_end = data[1].split(",")
    second_start, second_end = int(second_start), int(second_end)

    for number in range(first_start, first_end+1):
        first_set.add(number)

    for number in range(second_start, second_end + 1):
        second_set.add(number)

    if len(first_set.intersection(second_set)) > len(longest_intersection):
        longest_intersection = first_set.intersection(second_set)

    first_set = set()
    second_set = set()


print(f"Longest intersection is"
      f" [{', '.join(str(x) for x in longest_intersection)}] "
      f"with length {len(longest_intersection)}")
