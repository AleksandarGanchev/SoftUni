def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    shopping_dict = {}
    for product, values in kwargs.items():
        price, quantity = values
        bill = price * quantity
        if bill <= budget:
            shopping_dict[product] = bill
            budget -= bill
        if len(shopping_dict) == 5:
            break

    output = ''
    for product_name, total_price in shopping_dict.items():
        output += f"You bought {product_name} for {total_price:.2f} leva."'\n'

    return output

