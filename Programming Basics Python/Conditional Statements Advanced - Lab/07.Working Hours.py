working_hours = int(input())
day = input()

if 10 <= working_hours <= 18 and day == 'Monday':
        print('open')
elif 10 <= working_hours <= 18 and day == 'Tuesday':
        print('open')
elif 10 <= working_hours <= 18 and day == 'Wednesday':
        print('open')
elif 10 <= working_hours <= 18 and day == 'Thursday':
        print('open')
elif 10 <= working_hours <= 18 and day == 'Friday':
        print('open')
elif 10 <= working_hours <= 18 and day == 'Saturday':
        print('open')

else:
    print('closed')