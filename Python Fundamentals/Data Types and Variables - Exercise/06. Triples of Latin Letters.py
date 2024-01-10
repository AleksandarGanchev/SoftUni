num= int(input())

for x in range(num):
    for y in range(num):
        for z in range(num):
            print(f'{chr(97+x)}{chr(97+y)}{chr(97+z)}')