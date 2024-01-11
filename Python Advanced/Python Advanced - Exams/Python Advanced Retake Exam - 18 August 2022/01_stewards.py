from collections import deque

seats = input().split(", ")
first_integers = deque(int(x) for x in input().split(", "))
second_integers = deque(int(x) for x in input().split(", "))

rotations = 0
taken_seats = []
while rotations < 10 and len(taken_seats) < 3:

    first_number = first_integers.popleft()
    second_number = second_integers.pop()

    result = first_number + second_number
    char = chr(result)
    if str(first_number) + char in seats:
        if str(first_number) + char not in taken_seats:
            taken_seats.append(str(first_number)+char)

    elif str(second_number) + char in seats:
        if str(second_number) + char not in taken_seats:
            taken_seats.append(str(second_number)+char)

    else:
        first_integers.append(first_number)
        second_integers.appendleft(second_number)

    rotations += 1

print(f"Seat matches: {', '.join([str(x) for x in taken_seats])}")
print(f"Rotations count: {rotations}")
