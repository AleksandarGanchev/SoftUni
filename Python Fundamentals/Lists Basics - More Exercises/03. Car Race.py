numbers = [int(x) for x in  input().split() ]

total_len = len(numbers) -1
each_racer = total_len // 2
left_racer = 0
right_racer = 0

reversed_list = numbers[::-1]


for index in range( len(numbers)):
    if index == each_racer:
        break
    num = numbers[index]
    left_racer += num
    if num == 0:
        left_racer *= 0.8


for idx in range(len(reversed_list)):
    if idx == each_racer:
        break
    second_num = reversed_list[idx]
    right_racer += second_num
    if second_num == 0:
        right_racer *= 0.8

if left_racer < right_racer:
    print(f"The winner is left with total time: {left_racer:.1f}")
elif right_racer < left_racer:
    print(f"The winner is right with total time: {right_racer:.1f}")
