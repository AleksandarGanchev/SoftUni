import re

text_string = input()
pattern = r'(?P<symbol>[\@#])(?P<word>[A-Za-z]{3,})\1{2}(?P<s_word>[A-Za-z]{3,})'
matches = re.finditer(pattern,text_string)

word_pairs = []
mirror_pairs = []
for match in matches:
    symbols,word,second_word = match.groups()
    word_pairs.append(word)
    if word == second_word[::-1]:
        mirror_pairs.append(f'{word} <=> {second_word}')


if word_pairs:
    print(f"{len(word_pairs)} word pairs found!")
else:
    print("No word pairs found!")
if  not mirror_pairs:
    print("No mirror words!")
else:
    print('The mirror words are:')
    print(', '.join(mirror_pairs))