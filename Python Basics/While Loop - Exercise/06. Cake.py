length = int(input())
width = int(input())
taken_pieces = 0

total = length * width

while total > 0:
    command = input()
    if command == 'STOP':
        print(f"{total} pieces are left." )
        break
    else:
        total -= int(command)

if total < 0 :
     print(f"No more cake left! You need {abs(total)} pieces more.")