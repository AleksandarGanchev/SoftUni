import re
text = input()
result = 0
pattern = r'(::|\*\*)([A-Z][a-z]{2,})(\1)'
matches = re.findall(pattern,text)

cool_threshold = 1
for letter in text:
    if letter.isdigit():
        for number in letter:
            cool_threshold *= int(number)

found_emojis = []
dictionary_emojis = {}

for item in matches:
    emoji = ''.join(item)
    found_emojis.append(emoji)

    for letter in emoji:
        if letter.isalpha():
            result += ord(letter)
    dictionary_emojis[emoji] = result
    result = 0

print(f"Cool threshold: {cool_threshold}")

print(f"{len(dictionary_emojis)} emojis found in the text. The cool ones are:")

for k, v in dictionary_emojis.items():
    if v > cool_threshold:
        print(k)
