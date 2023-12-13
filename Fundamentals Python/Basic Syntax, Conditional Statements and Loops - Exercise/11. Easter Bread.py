budget = float(input())
flour_price = float(input())

milk_price_per_liter = flour_price * 1.25
eggs_price_per_pack = flour_price * 0.75

loafs = 0
colored_eggs = 0
while True:
    milk_per_bread = milk_price_per_liter / 4
    products_for_one_bread = flour_price + milk_per_bread + eggs_price_per_pack

    if budget - products_for_one_bread > 0:
        budget -= products_for_one_bread
        loafs += 1
        colored_eggs += 3
        if loafs % 3 == 0:
            colored_eggs -= (loafs - 2)
    else:
        break

print(f"You made {loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

