exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minute = int(input())


exam_time_in_minutes = exam_hour * 60 + exam_minutes
exam_arrival_in_minutes = arrival_hour * 60 + arrival_minute


diff = abs(exam_time_in_minutes - exam_arrival_in_minutes)
hours = diff // 60
minutes = diff % 60

if exam_time_in_minutes == exam_arrival_in_minutes:
    print('On time')



if exam_time_in_minutes > exam_arrival_in_minutes:
    if diff <= 30:
        print(f'On time {minutes} minutes before the start')
    elif diff <= 59:
        print('Early')
        print(f'{diff} minutes before the start')
    elif diff >= 60:
        print('Early')
        print(f'{hours:}:{minutes:02d} hours before the start')

if exam_time_in_minutes < exam_arrival_in_minutes:
    if diff <= 59:
        print('Late')
        print(f'{diff} minutes after the start')
    elif diff >= 60:
        print('Late')
        print(f'{hours}:{minutes:02d} hours after the start')