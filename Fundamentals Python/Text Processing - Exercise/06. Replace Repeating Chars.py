string = input()

result = string[0]
for letter in string:
    if letter == result[-1]:
        continue
    else:
        result += letter

print(result)