age = int(input())
drink_type= ''

if age <= 14:
   drink_type = 'drink toddy'
elif age <= 18:
    drink_type = 'drink coke'
elif age <= 21:
    drink_type = 'drink beer'
elif age >= 22:
    drink_type = 'drink whisky'

print(drink_type)