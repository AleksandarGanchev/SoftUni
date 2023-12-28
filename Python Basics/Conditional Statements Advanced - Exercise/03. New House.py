flower_type = input()
flowers_count = int(input())
budget = int(input())
price = 0

if flower_type == 'Roses':
    price = 5
    if flowers_count > 80 :
        price = 5 - 5 * 0.10

elif flower_type == 'Dahlias':
    price = 3.80
    if flowers_count > 90 :
        price = 3.80 - 3.80 * 0.15

elif flower_type == 'Tulips':
    price = 2.80
    if flowers_count > 80 :
        price = 2.80 - 2.80 * 0.15

elif flower_type == 'Narcissus':
    price = 3
    if flowers_count < 120 :
        price = 3 + 3 * 0.15

elif flower_type == 'Gladiolus':
    price = 2.50
    if flowers_count < 80 :
        price = 2.50 + 2.50 * 0.20


expenses = flowers_count * price
total = budget - flowers_count * price

if budget >= expenses :
    print(f"Hey, you have a great garden with {flowers_count} {flower_type} and {total:.2f} leva left.")

else:
    print(f"Not enough money, you need {abs(total):.2f} leva more.")