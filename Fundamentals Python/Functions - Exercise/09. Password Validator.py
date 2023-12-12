def length(password):
    return 6 <= len(password) <= 10

def only_letter_n_num(password):
    return password.isalnum()

def at_least_two(password):
    digits_counter = 0
    for ch in password:
        if ch.isdigit():
            digits_counter += 1

    return  digits_counter >= 2

input_password = input()
incorrect_data = []
if not length(input_password):
    incorrect_data.append("Password must be between 6 and 10 characters")

if not only_letter_n_num(input_password):
    incorrect_data.append('Password must consist only of letters and digits')


if not at_least_two(input_password):
    incorrect_data.append("Password must have at least 2 digits")


if len(incorrect_data) <= 0:
    print('Password is valid')

else:
    print("\n".join(incorrect_data))