rows, cols = [int(x) for x in input().split(', ')]

total_decorations, total_gifts, total_cookies = 0, 0, 0
collected_decorations, collected_gifts, collected_cookies = 0, 0, 0
y_row, y_col = [0, 0]

workshop = []
for row in range(rows):
    workshop.append(input().split())
    total_decorations += workshop[row].count('D')
    total_gifts += workshop[row].count('G')
    total_cookies += workshop[row].count('C')
    if 'Y' in workshop[row]:
        y_row, y_col = row, workshop[row].index('Y')
        workshop[y_row][y_col] = 'x'

all_collected = False
command = input()
while command != "End":
    direction, steps = command.split('-')
    steps = int(steps)

    for step in range(steps):
        if direction == "up":
            y_row -= 1
            if y_row == -1:
                y_row = rows - 1
        elif direction == "down":
            y_row += 1
            if y_row == rows:
                y_row = 0
        if direction == "left":
            y_col -= 1
            if y_col == -1:
                y_col = cols - 1
        elif direction == "right":
            y_col += 1
            if y_col == cols:
                y_col = 0

        if workshop[y_row][y_col] == 'D':
            collected_decorations += 1
        elif workshop[y_row][y_col] == 'G':
            collected_gifts += 1
        elif workshop[y_row][y_col] == 'C':
            collected_cookies += 1

        workshop[y_row][y_col] = 'x'

        if (total_decorations == collected_decorations and total_gifts == collected_gifts and
           total_cookies == collected_cookies):
            print("Merry Christmas!")
            all_collected = True
            break

    if all_collected:
        break
    command = input()

workshop[y_row][y_col] = 'Y'

print("You've collected:")
print(f"- {collected_decorations} Christmas decorations")
print(f"- {collected_gifts} Gifts")
print(f"- {collected_cookies} Cookies")
[print(*i) for i in workshop]
