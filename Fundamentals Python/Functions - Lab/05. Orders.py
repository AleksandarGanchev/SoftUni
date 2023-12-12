def calculate(product_type, quantity_times):

    total_amount = 0
    if product_type == 'coffee':
        total_amount = 1.50 * quantity_times
    elif product_type == 'water':
        total_amount = 1.00 * quantity_times
    elif product_type == 'coke':
        total_amount = 1.40 * quantity_times
    elif product_type == 'snacks':
        total_amount = 2.00 * quantity_times

    return total_amount

products_to_buy = input()
quantity_to_buy = int(input())

result = calculate(products_to_buy, quantity_to_buy)
print(f'{result:.2f}')