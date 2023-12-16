def miner_task(resource):
    mining = {}
    while resource != "stop":
        quantity = int(input())
        if resource not in mining:
            mining[resource] = quantity
        else:
            mining[resource] += quantity

        resource = input()

    return mining


resource = input()
mining = (miner_task(resource))

for k, v in mining.items():
    print(f"{k} -> {v}")
