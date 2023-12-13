waiting_people = int(input())
wagon_places = [int(x) for x in input().split()]
wagon_index = len(wagon_places)
people_to_add = 4
possible_people = 0


for el in range(wagon_index):
    person_index = el % wagon_index
    possible_people = people_to_add - wagon_places[el]

    if waiting_people >= people_to_add:
        wagon_places[el] += possible_people
        waiting_people -= possible_people

    elif people_to_add > waiting_people:
        wagon_places[el] += waiting_people
        waiting_people -= waiting_people

if waiting_people == 0 and wagon_places[el] != 4:
    print("The lift has empty spots!")
    print(' '.join(str(x) for x in wagon_places))

elif waiting_people > 0 and wagon_places[el] == 4:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(' '.join(str(x) for x in wagon_places))


elif waiting_people == 0 and wagon_places[el] == 4:
    print(' '.join(str(x) for x in wagon_places))
