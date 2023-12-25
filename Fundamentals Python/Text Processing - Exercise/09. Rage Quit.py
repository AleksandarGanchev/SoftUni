def rage_quit(data):
    i = 0
    rage_message = ""
    unique_symbols = set()

    while i < len(data):
        current_string = ""
        while i < len(data) and not data[i].isdigit():
            unique_symbols.add(data[i].upper())
            current_string += data[i].upper()
            i += 1

        repeat_count = 0
        while i < len(data) and data[i].isdigit():
            repeat_count = repeat_count * 10 + int(data[i])
            i += 1

        rage_message += current_string * repeat_count

    print(f"Unique symbols used: {len(unique_symbols)}")
    print(rage_message)


string = input()

rage_quit(string)





# string = input()
# letters = ""
# final_message = ""
# number = 0
#
# next_is_digit = False
# for index in range(len(string)):
#     if not string[index].isdigit():
#         next_is_digit = False
#         letters += string[index]
#     else:
#         if not next_is_digit:
#             number = string[index]
#         if index + 1 < len(string):
#             if string[index+1].isdigit():
#                 number += string[index+1]
#                 next_is_digit = True
#         number = int(number)
#         final_message += letters * number
#         letters = ""
#
# final_message = final_message.upper()
# print(f"Unique symbols used: {len(set(final_message))}")
# print(f"{final_message}")
