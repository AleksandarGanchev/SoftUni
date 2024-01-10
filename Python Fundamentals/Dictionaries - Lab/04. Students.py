dictionary = {}
data = input()
while True:
    data_args = data.split(':')
    if len(data_args) == 1:
        break

    name, id, course = data_args
    if  not course in dictionary.keys():
        dictionary[course] = {name: id}
    else:
        dictionary[course][name] = id

    data = input()

data = data.split('_')
data = ' '.join(data)
students = dictionary[data]

for name, id in students.items():
    if data in dictionary.keys():
        print(f"{name} - {id}" )