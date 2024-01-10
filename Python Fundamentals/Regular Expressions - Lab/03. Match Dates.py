import re
phone_numbers = input()

matches = r'(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})'
result = re.findall(matches, phone_numbers)

for match in result:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")