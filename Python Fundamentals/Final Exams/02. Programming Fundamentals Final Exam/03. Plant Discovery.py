plant_discovery = {}

result = 0
n = int(input())
for _ in range(n):
    data = input()
    data = data.split('<->')
    plant, rarity = data
    rarity = int(rarity)
    plant_discovery[plant] = [rarity, []]

command = input()
while command != 'Exhibition':
    command = command.split(': ')
    if command[0] == 'Rate':
        plant,rating = command[1].split(' - ')
        rating = int(rating)
        if plant not in plant_discovery:
            print('error')
        else:
               plant_discovery[plant][1].append(rating)

    elif command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        if plant not in plant_discovery:
            print('error')
        else:
            plant_discovery[plant][0] = new_rarity

    elif command[0] == 'Reset':
        reset_plant = command[1]
        if reset_plant not in plant_discovery:
            print('error')
        else:
            plant_discovery[reset_plant][1] = []

    command = input()

print('Plants for the exhibition:')
for k, value in plant_discovery.items():
    if len(value[1]):
        result = sum(value[1]) / len(value[1])
    else:
        result = 0
    print(f'- {k}; Rarity: {value[0]}; Rating: {result:.2f}')