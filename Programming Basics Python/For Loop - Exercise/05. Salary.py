open_tabs = int(input())
salary = int(input())

for _ in range(open_tabs):
    tabs = input()
    if tabs == 'Facebook':
        salary -= 150
    elif tabs == 'Instagram':
        salary -= 100
    elif tabs == 'Reddit':
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

else:
    print(f'{salary}')