collection_items = input().split('|')
budget = int(input())
bought_items = 0
sold_items = 0
sold_prices = []
for command in collection_items:
    command_args = command.split('->')
    item = command_args[0]
    price = float(command_args[1])

    if item == 'Clothes' and price > 50.00:
        continue

    if item == 'Shoes' and price > 35.00:
        continue

    if item == 'Accessories' and price > 20.50:
        continue

    if price > budget:
        continue

    budget -= price
    bought_items += price
    sold_items_price = price * 1.4
    sold_items += sold_items_price
    sold_prices.append(sold_items_price)

profit = sold_items - bought_items

for sold in sold_prices:
    print(f'{sold:.2f}',end= ' ')

print()
print(f'Profit: {profit:.2f}')

if sold_items + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')