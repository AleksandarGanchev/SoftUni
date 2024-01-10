import re
text = input()
occurrences_word = input()

pattern = fr'\b{occurrences_word}\b'
matches =re.findall(pattern, text, re.IGNORECASE)

print(len(matches))
