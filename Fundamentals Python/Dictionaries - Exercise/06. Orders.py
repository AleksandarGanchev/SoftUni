dictionary = {}

data = input()
while data != 'buy':
    data = data.split()
    product, price, quantity = data
    price = float(price)
    quantity = int(quantity)

    if product not in dictionary:
        dictionary[product] = [price, quantity]

    else:
        dictionary[product][0] = price
        dictionary[product][1] += quantity

    data = input()

for k, v in dictionary.items():
    print(f"{k} -> {v[0] * v[1]:.2f}")
