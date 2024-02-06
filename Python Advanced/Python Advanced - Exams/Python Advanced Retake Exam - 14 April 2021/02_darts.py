def is_first_player_turn(turns_number):
    if turns_number % 2 != 0:
        return True


def field_row_col_edges(r, c, matrix):
    edges_sum = matrix[0][c] + matrix[-1][c] + matrix[r][0] + matrix[r][-1]
    return edges_sum


first_player, second_player = input().split(", ")
SIZE = 7
darts = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(7)]

first_points = 501
second_points = 501

first_turns = 0
second_turns = 0
total_turns = 0
while first_points > 0 and second_points > 0:
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    total_turns += 1
    if is_first_player_turn(total_turns):
        first_turns += 1
    else:
        second_turns += 1

    try:
        darts[row][col]
    except IndexError:
        continue

    if darts[row][col] == 'B':
        if is_first_player_turn(total_turns):
            print(f"{first_player} won the game with {first_turns} throws!")
        else:
            print(f"{second_player} won the game with {second_turns} throws!")
        break

    if isinstance(darts[row][col], int):
        if is_first_player_turn(total_turns):
            first_points -= darts[row][col]
        else:
            second_points -= darts[row][col]

    elif darts[row][col] == 'D':
        result = field_row_col_edges(row, col, darts) * 2
        if is_first_player_turn(total_turns):
            first_points -= result
        else:
            second_points -= result

    elif darts[row][col] == 'T':
        result = field_row_col_edges(row, col, darts) * 3
        if is_first_player_turn(total_turns):
            first_points -= result
        else:
            second_points -= result


else:
    if first_points <= 0:
        print(f"{first_player} won the game with {first_turns} throws!")
    else:
        print(f"{second_player} won the game with {second_turns} throws!")
