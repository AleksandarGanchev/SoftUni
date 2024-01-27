def grocery_store(**kwargs):
    result = []
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for product, quantity in kwargs:
        result.append(f"{product}: {quantity}")

    return '\n'.join(result)
