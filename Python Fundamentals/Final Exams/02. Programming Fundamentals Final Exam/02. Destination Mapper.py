import re
text = input()

pattern = r'([=/])([A-Z][A-Za-z]{2,})\1'
matches = re.finditer(pattern, text)

destionations_list = []
total_len = 0
for match in matches:
    regex = match.group(1)
    destionations = match.group(2)
    total_len += len(destionations)
    destionations_list.append(destionations)


print(f"Destinations: {', '.join(destionations_list)}" )
print(f"Travel Points: {total_len}")
