degrees = int(input())
time= input()
Outfit = ''
Shoes = ''

if 10 <= degrees <= 18:
    Outfit = 'Sweatshirt' if time == 'Morning' else 'Shirt'
    Shoes = 'Sneakers' if time == 'Morning' else 'Moccasins'

elif 19 <= degrees <= 24:
    Outfit = 'T-Shirt' if time == 'Afternoon' else 'Shirt'
    Shoes = 'Sandals' if time == 'Afternoon' else 'Moccasins'

else:
    Outfit = 'T-Shirt' if time == 'Morning' else 'Swim Suit' if time == 'Afternoon' else 'Shirt'
    Shoes = 'Sandals' if time == 'Morning' else 'Barefoot' if time == 'Afternoon' else 'Moccasins'

print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")