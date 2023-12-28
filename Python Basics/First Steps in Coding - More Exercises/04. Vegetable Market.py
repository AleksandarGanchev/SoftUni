price_per_kg_veggies = float(input())
price_per_kg_fruits = float(input())
quantity_kg_veggies = int(input())
quantity_kg_fruits = int(input())
euro_to_lev = 1.94

total_veggies = price_per_kg_veggies * quantity_kg_veggies
total_fruits = price_per_kg_fruits *  quantity_kg_fruits

total_price_in_lev = total_fruits + total_veggies
total_price_in_euro = total_price_in_lev / euro_to_lev
print(f"{total_price_in_euro:.2f}")