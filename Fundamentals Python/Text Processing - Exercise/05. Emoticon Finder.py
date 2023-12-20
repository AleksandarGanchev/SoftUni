data = input()

for index, letter in enumerate(data):
    if letter == ':' :
        print(f':{data[index+1]}')