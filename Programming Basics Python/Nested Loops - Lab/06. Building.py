floors_count = int(input())
rooms_count = int(input())
room = ''

for floor in reversed(range(1, floors_count +1)):
    print()
    if floor == floors_count:
        room = 'L'
    elif floor % 2 == 0:
        room = 'O'
    elif floor % 2 != 0:
        room = 'A'
    for rooms in range(rooms_count):


        print(f'{room}{floor}{rooms}', end = ' ')
