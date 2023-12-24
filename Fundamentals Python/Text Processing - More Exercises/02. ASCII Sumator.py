first_char_symbol = input()
second_char_symbol = input()
random_string = input()

first_char_number = ord(first_char_symbol)
second_char_number = ord(second_char_symbol)

result = 0
for el in random_string:
    if el.isdigit():
        if ord(first_char_symbol) < ord(el) < ord(second_char_symbol):
            result += ord(el)
    else:
        if first_char_number < ord(el) < second_char_number:
            result += ord(el)

print(result)
