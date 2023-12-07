budget = int(input())
season = input()
fisherman_count = int(input())
rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or  season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fisherman_count <= 6:
    rent = rent - rent * 0.10
elif 7 <= fisherman_count <= 11:
    rent = rent - rent * 0.15
elif fisherman_count >= 12:
    rent = rent - rent * 0.25

if fisherman_count % 2 == 0 and season != 'Autumn':
    rent = rent - rent * 0.05

total = abs(budget - rent)

if budget < rent :
    print(f"Not enough money! You need {total:.2f} leva. ")



else:
    print(f"Yes! You have {total:.2f} leva left. ")