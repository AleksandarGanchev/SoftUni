from math import floor


first = int(input())
second = int(input())
third = int(input())


total_seconds = first + second + third
minutes = total_seconds // 60
seconds = total_seconds % 60

minutes = floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
