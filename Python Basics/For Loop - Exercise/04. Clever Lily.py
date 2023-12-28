age = int(input())
machine_price = float(input())
toys_price = int(input())
toys_count = 0
savings = 0
money = 0
money_for_year = 10

for i in range(1, age +1):
    if i % 2 == 0:
        money += money_for_year - 1
        money_for_year += 10

    else:
        toys_count += 1


savings = money + toys_price * toys_count

diff = abs(savings - machine_price)

if savings >= machine_price:
    print(f'Yes! {diff:.2f}')

else:
    print(f'No! {diff:.2f}')