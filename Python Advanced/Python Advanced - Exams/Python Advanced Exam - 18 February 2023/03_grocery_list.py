def shop_from_grocery_list(budget: int, groceries: list, *args: tuple):
    for product, price in args:
        if len(groceries) == 0:
            break

        if product in groceries:
            if price > budget:
                break

            budget -= price
            groceries.remove(product)

    if len(groceries):
        return f"You did not buy all the products. Missing products: {', '.join([str(x) for x in groceries])}."

    return f"Shopping is successful. Remaining budget: {budget:.2f}."
