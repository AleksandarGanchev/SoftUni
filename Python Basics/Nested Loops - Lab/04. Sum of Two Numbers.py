first_number = int(input())
second_number = int(input())
magic_number = int(input())
combination = 0
is_found = False

for x in range(first_number, second_number + 1):
    for y in range(first_number,second_number +1):
        combination += 1
        if x + y == magic_number:
            is_found = True
            print(f"Combination N:{combination} ({x} + {y} = {magic_number})")
            break

    if is_found:
        break

else:
        print(f"{combination} combinations - neither equals {magic_number}")