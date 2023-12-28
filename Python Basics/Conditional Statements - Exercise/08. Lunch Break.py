import math

tv_show = input()
episode_length = int(input())
break_length = int(input())
lunch_time = 1/8 * break_length
rest_time = 1/4 * break_length

total = break_length - lunch_time - rest_time #37.5
free_time = math.ceil(abs(break_length - lunch_time -rest_time - episode_length))


if total >= episode_length :
    print(f"You have enough time to watch {tv_show} and left with {free_time} minutes free time.")

else:
    print(f"You don't have enough time to watch {tv_show}, you need {free_time} more minutes.")