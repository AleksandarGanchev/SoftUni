legendary_farming = {"shards":0, "fragments":0, "motes":0}
junk_items = {}
flag = True
while flag:
    data = input().split()
    for element in range(0, len(data)-1, 2):
        quantity = int(data[element])
        material = data[element+1].lower()

        if material == "shards":
            legendary_farming[material] += quantity
            if legendary_farming[material] >= 250:
                print("Shadowmourne obtained!")
                legendary_farming[material] -= 250
                flag = False
                break

        elif material == "fragments":
            legendary_farming[material] += quantity
            if legendary_farming[material] >= 250:
                print("Valanyr obtained!")
                legendary_farming[material] -= 250
                flag = False
                break

        elif material == "motes":
            legendary_farming[material] += quantity
            if legendary_farming[material] >= 250:
                print("Dragonwrath obtained!")
                legendary_farming[material] -= 250
                flag = False
                break

        else:
            if material not in junk_items:
                junk_items[material] = quantity
            else:
                junk_items[material] += quantity

for k, v in legendary_farming.items():
    print(f"{k}: {v}")


for k, v in junk_items.items():
    print(f"{k}: {v}")



