command = input()
total_price = 0
taxes = 0
total_price_with_tax = 0

while command != 'special' and command != 'regular':
    part_price = float(command)
    if part_price < 0:
        print("Invalid price!")

    elif part_price > 0:
        total_price += part_price
        taxes += (part_price * 0.2)

    command = input()

if total_price == 0:
    print("Invalid order!")

if total_price > 0:
    total_price_with_tax = total_price + taxes
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print('-----------')
    if command != 'special':
        print(f"Total price: {total_price_with_tax:.2f}$")

    if command == 'special':
        print(f"Total price: {total_price_with_tax * 0.9:.2f}$")