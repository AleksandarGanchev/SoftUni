text = input()
forbidden_letters = 'a', 'o', 'u', 'e', 'i'
result = [char for char in text if char.lower() not in forbidden_letters]
print(''.join(result))
