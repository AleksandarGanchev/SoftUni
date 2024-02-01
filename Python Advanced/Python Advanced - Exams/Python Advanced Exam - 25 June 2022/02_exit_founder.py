from collections import deque
players = deque(input().split(", "))
maze = []
for row in range(6):
    maze.append(input().split())

jerry_punished = False
tom_punished = False
while True:
    player_position = input()
    p_row = int(player_position[1])
    p_col = int(player_position[4])

    if players[0] == "Jerry" and jerry_punished:
        jerry_punished = False
        players.rotate()
        continue

    if players[0] == "Tom" and tom_punished:
        tom_punished = False
        players.rotate()
        continue

    if maze[p_row][p_col] == 'E':
        print(f"{players[0]} found the Exit and wins the game!")
        break

    elif maze[p_row][p_col] == 'W':
        if players[0] == "Jerry":
            jerry_punished = True
        elif players[0] == "Tom":
            tom_punished = True
        print(f"{players[0]} hits a wall and needs to rest.")

    elif maze[p_row][p_col] == 'T':
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break

    players.rotate()
