from math import pi


figure = input('square or rectangle or circle or triangle:')
total = 0
if figure == 'square':
    a = float(input())
    total = a * a

elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    total = a * b

elif figure == 'circle':
    a = float(input())
    total = pi * ( a ** 2)


elif figure == 'triangle':
    a = float(input())
    b = float(input())
    total = 1/2 * a * b

print(f'{total:.3f}')