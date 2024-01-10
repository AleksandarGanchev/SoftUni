key = int(input())
n = int(input())

new_word = ''
for _ in range(n):
    letter = input()
    curr_number = ord(letter)
    curr_letter = chr(curr_number+key)
    new_word += curr_letter

print(new_word)