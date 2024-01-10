data = input()

occ = {}

for char in data:
    if char not in occ:
        occ[char] = 0
    occ[char] += 1

for char, count in sorted(occ.items()):
    print(f"{char}: {count} time/s")
