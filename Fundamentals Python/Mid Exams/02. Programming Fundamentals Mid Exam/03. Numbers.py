numbers = [int(x) for x in (sorted(input().split()))]
largest_numbers = []
total_sum = sum(numbers)
average = total_sum / len(numbers)

flag = False
counter = 0
for number in reversed(numbers):
    if number > average:
        if counter < 5:
            largest = max(numbers)
            numbers.remove(max(numbers))
            largest_numbers.append(largest)
            counter += 1
            flag = True


if flag:
    print(*largest_numbers,sep=' ')
else:
    print('No')