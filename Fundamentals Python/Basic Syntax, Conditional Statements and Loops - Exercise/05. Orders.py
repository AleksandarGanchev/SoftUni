orders_number = int(input())
price_per_day = 0
total_price = 0
for i in range(orders_number):
    price_per_casule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if 0.01 <= price_per_casule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        price_per_day = price_per_casule * days * capsules_needed_per_day
        print(f"The price for the coffee is: ${price_per_day:.2f}")
        total_price += price_per_day
        price_per_day = 0

print(f"Total: ${total_price:.2f}")