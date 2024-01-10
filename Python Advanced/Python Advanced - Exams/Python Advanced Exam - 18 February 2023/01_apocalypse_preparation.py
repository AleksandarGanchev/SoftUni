from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
          }

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    item = textile + medicament

    if item == 30:
        created_items["Patch"] += 1
    elif item == 40:
        created_items["Bandage"] += 1
    elif item == 100:
        created_items["MedKit"] += 1
    elif item > 100:
        created_items["MedKit"] += 1
        medicaments[-1] += (item-100)
    else:
        medicaments.append(medicament+10)
sorted_items = sorted(created_items.items(), key= lambda x: (-x[1], x[0]))
if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
    for item in sorted_items:
        if item[1] > 0:
            print(f"{item[0]} - {item[1]}")

elif not textiles:
    print("Textiles are empty.")
    for item in sorted_items:
        if item[1] > 0:
            print(f"{item[0]} - {item[1]}")

    medicaments = reversed(medicaments)
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments])}")

elif not medicaments:
    print("Medicaments are empty.")
    for item in sorted_items:
        if item[1] > 0:
            print(f"{item[0]} - {item[1]}")
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
