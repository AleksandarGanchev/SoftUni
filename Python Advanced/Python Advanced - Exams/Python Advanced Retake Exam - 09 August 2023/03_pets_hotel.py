def accommodate_new_pets(capacity, maximum_weight, *args):
    terminated = False
    new_pets = {}
    accommodated_pets = 0
    for pet_type, pet_weight in args:
        if capacity - accommodated_pets <= 0:
            terminated = True
            break

        if pet_weight <= maximum_weight:
            if pet_type not in new_pets:
                new_pets[pet_type] = []

            new_pets[pet_type].append(pet_weight)
            accommodated_pets += 1

    sorted_pets = dict(sorted(new_pets.items(), key=lambda x: (len(x[0]), x[1])))

    if terminated:
        output = f"You did not manage to accommodate all pets!"'\n'
    else:
        output = f"All pets are accommodated! Available capacity: {capacity - accommodated_pets}."'\n'

    output += f"Accommodated pets:"'\n'
    for pet_kind, pet_number in sorted_pets.items():
        output += f"{pet_kind}: {len(pet_number)}\n"

    return output










