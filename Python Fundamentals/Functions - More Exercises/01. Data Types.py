def data_types(data_type, input):
    result = ''
    if data_type == "int":
        result = int(input) * 2

    elif data_type == "real":
        result = f"{float(input) * 1.5:.2f}"

    elif data_type == "string":
        result = f"${input}$"

    return result

data_type = input()
input = input()
print(data_types(data_type, input))





