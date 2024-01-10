n = int(input())
name_start_index = 0
name_end_index = 0
age_start_index = 0
age_end_index = 0

for _ in range(n):
    text = input()

    for index in range(len(text)):
        if text[index] == "@":
            name_start_index = index + 1
        elif text[index] == "|":
            name_end_index = index

        elif text[index] == "#":
            age_start_index = index + 1
        elif text[index] == "*":
            age_end_index = index

    name = text[name_start_index:name_end_index]
    age = text[age_start_index:age_end_index]

    print(f"{name} is {age} years old.")
