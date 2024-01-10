n = int(input())
piano_dictionary = {}
for _ in range(n):
    data = input()
    piece, composer, key = data.split('|')
    piano_dictionary[piece] = [composer, key]

command = input()
while command != 'Stop':
    data_args = command.split('|')
    if data_args[0] == 'Add':
        add, piece, composer, key = data_args
        if piece in piano_dictionary:
            print(f"{piece} is already in the collection!")
        else:
            piano_dictionary[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif data_args[0] == 'Remove':
        remove, piece = data_args
        if piece in piano_dictionary:
            del piano_dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif data_args[0] == 'ChangeKey':
        change_key, piece, new_key = data_args
        if piece in piano_dictionary:
            piano_dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for k, v in piano_dictionary.items():
    print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")