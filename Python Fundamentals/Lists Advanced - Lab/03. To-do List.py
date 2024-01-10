command = input()
list = [0] * 10
while command != 'End':
    importance, note = command.split('-')
    importance = int(importance)
    index = importance - 1
    list[index] = note
    command = input()

print( [note for note in list if note != 0])