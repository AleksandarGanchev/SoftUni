data = input().split()

counter = 0
command = input()
while command != 'end':
    counter += 1
    first,second = command.split()
    first = int(first)
    second = int(second)
    length = len(data) // 2

    if first == second or not 0 <= first < len(data) or not 0 <= second < len(data):
        print("Invalid input! Adding additional elements to the board")
        data.insert(length, f"-{counter}a" )
        data.insert(length, f"-{counter}a" )

    elif data[first] == data[second]:
        print(f"Congrats! You have found matching elements - {data[first]}!")
        del data[first]
        if first < second:
            second -= 1
        del data[second]

    else:
        print("Try again!")

    if not len(data):
        print(f"You have won in {counter} turns!")
        break

    command = input()

if len(data):
    print(f'Sorry you lose :(')
    print(' '.join(data))