SIZE = 6
matrix = [[x if x.isalpha() else int(x) for x in input().split()]for _ in range(SIZE)]

points = 0
for throws in range(3):
    f_data, s_data = input().split(', ')
    rows = int(f_data[1:])
    cols, _ = s_data.split(')')
    cols = int(cols)

    try:
        symbol = matrix[rows][cols]
        matrix[rows][cols] = 0

    except IndexError:
        continue

    if symbol == 'B':
        for row in range(SIZE):
            points += matrix[row][cols]

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")








