project_type = input()
rows = int(input())
columns = int(input())
price = 0

if project_type == 'Premiere':
    price = 12
elif project_type == 'Normal':
    price = 7.50
elif project_type == 'Discount':
    price = 5


total = rows * columns * price
print(f'{total:.2f} leva')
