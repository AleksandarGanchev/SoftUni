from collections import deque


def best_list_pureness(numbers, rotations):
    numbers = deque(numbers)
    best_rotation = 0
    best_pureness = float('-Inf')
    for rotation in range(rotations+1):
        current_pureness = 0

        for index, number in enumerate(numbers):
            current_pureness += number * index
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotation
        numbers.rotate(1)

    return f"Best pureness {best_pureness} after {best_rotation} rotations"
