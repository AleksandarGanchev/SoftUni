dictionary = {}

command = input()
while command != 'Sail':
    command = command.split("||")
    city, population, gold = command
    population = int(population)
    gold = int(gold)

    if city not in dictionary:
        dictionary[city] = [population, gold]
    else:
        dictionary[city][0] += population
        dictionary[city][1] += gold

    command = input()

data = input()
while data != 'End':
    data = data.split('=>')
    if data[0] == 'Plunder':
        plunder, town, people, stolen_gold = data
        people = int(people)
        stolen_gold = int(stolen_gold)
        if town in dictionary:
            dictionary[town][0] -= people
            dictionary[town][1] -= stolen_gold
            print(f"{town} plundered! {stolen_gold} gold stolen, {people} citizens killed.")

            if dictionary[town][0] == 0 or dictionary[town][1] == 0:
                del dictionary[town]
                print(f"{town} has been wiped off the map!")

    elif data[0] == 'Prosper':
        prosper, town, add_gold = data
        add_gold = int(add_gold)
        if add_gold < 0:
            print("Gold added cannot be a negative number!")
        elif add_gold > 0:
            dictionary[town][1] += add_gold
            print(f"{add_gold} gold added to the city treasury. {town} now has {dictionary[town][1]} gold.")

    data = input()

if dictionary:
    print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
    for k,v in dictionary.items():
        print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")