current_hour = int(input())
current_minutes = int(input())

total_minutes = current_hour * 60 + current_minutes + 15

hours = total_minutes // 60
minutes = total_minutes % 60

if hours > 23:
    hours = 0

if minutes < 10 :
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')