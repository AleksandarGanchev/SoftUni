data = input()
result = ''

for letter in data:
    number = ord(letter) + 3
    char = chr(number)
    result += char

print(result)