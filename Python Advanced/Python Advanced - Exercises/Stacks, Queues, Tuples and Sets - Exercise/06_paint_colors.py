from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

combinations = []
while words:
    first_string = words.popleft()
    second_string = words.pop() if words else ''

    for color in (first_string + second_string, second_string + first_string):
        if color in colors:
            combinations.append(color)
            break

    else:
        for el in (first_string[:-1], second_string[:-1]):
            if el:
                words.insert(len(words) // 2, el)


for color in set(secondary_colors.keys()).intersection(combinations):
    if not secondary_colors[color].issubset(combinations):
        combinations.remove(color)

print(combinations)
