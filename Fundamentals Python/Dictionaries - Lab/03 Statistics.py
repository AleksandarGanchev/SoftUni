sum_quantity = 0

bakery = {}
command = input()
while command != 'statistics':
    command_args = command.split(': ')
    product = command_args[0]
    quantity = int(command_args[1])

    if not product in bakery:
        bakery[product] = quantity
    else:
        bakery[product] += quantity

    command = input()

print('Products in stock:')
for product, quantity in bakery.items():
    sum_quantity += quantity
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(bakery)}')
print(f'Total Quantity: {sum_quantity}')