input_line = input()
is_prime = True
non_prime_sum = 0
prime_sum = 0

while input_line != 'stop':

    curr_number = int(input_line)
    if curr_number < 0:
        print("Number is negative.")
    else:
        for i in range(2, curr_number):
            if curr_number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += curr_number
        else:
            non_prime_sum += curr_number
            is_prime = True

    input_line = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")