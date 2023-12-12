rooms = int(input())
flag = True
total_chairs = 0
total_visitors = 0
for room in range(1,rooms+1):
    command_args = input().split(' ')
    chairs = len(command_args[0])
    visitors = int(command_args[1])
    total_chairs += chairs
    total_visitors += visitors
    if visitors > chairs:
        print(f"{visitors-chairs} more chairs needed in room {room}")
        flag = False


if flag:
    print(f"Game On, {total_chairs - total_visitors} free chairs left")