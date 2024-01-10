import re

phone_numbers = input()

matches = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

result = re.findall(matches, phone_numbers)
print(', '.join(result))