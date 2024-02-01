def shopping_cart(*args):
    flag = False
    result = {
                "Soup": set(),
                "Pizza": set(),
                "Dessert": set()
            }
    for data in args:
        if data == "Stop":
            break
        else:
            flag = True
            meal_type, product = data
            if meal_type == "Soup" and len(result[meal_type]) < 3:
                result[meal_type].add(product)
            elif meal_type == "Pizza" and len(result[meal_type]) < 4:
                result[meal_type].add(product)
            elif meal_type == "Dessert" and len(result[meal_type]) < 2:
                result[meal_type].add(product)

    output = ''
    if flag:
        sorted_result = sorted(result.items(), key=lambda x: (-len(x[1]), x[0]))
        for meal, products in sorted_result:
            output += f"{meal}:"'\n'
            for product in sorted(products):
                output += f" - {product}"'\n'

        return output

    output = "No products in the cart!"
    return output
