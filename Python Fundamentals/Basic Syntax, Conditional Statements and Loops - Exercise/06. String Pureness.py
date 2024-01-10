n = int(input())
string_rules = { 'banned_symbols': ['.' , ',' , '_']}
for words in range(n):
    current_word = input()
    for letter in current_word:
        if letter in string_rules['banned_symbols']:
            print(f'{current_word} is not pure!')
            break
    else:
        print(f"{current_word} is pure.")