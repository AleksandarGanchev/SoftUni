import re

command = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
total_money = 0
bought_furniture = []
while command != 'Purchase':
    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        total_money += float(price) * int(quantity)
        bought_furniture.append(furniture)

    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)


print(f'Total money spend: {total_money:.2f}')