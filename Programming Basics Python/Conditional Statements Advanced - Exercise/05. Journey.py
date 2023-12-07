budget = float(input())
season = input()
expenses = 0
place  = ''
destination = ''

if budget <= 100 and season == 'summer':
    destination = 'Bulgaria'
    place = 'Camp'
    expenses = budget * 0.3
elif budget <= 100 and season == 'winter':
    destination = 'Bulgaria'
    place = 'Hotel'
    expenses = budget * 0.7

elif budget <= 1000 and season == 'summer':
    destination = 'Balkans'
    place = 'Camp'
    expenses = budget * 0.4
elif budget <= 1000 and season == 'winter':
    destination = 'Balkans'
    place = 'Hotel'
    expenses = budget * 0.8

elif budget > 1000 and season == 'summer' or season == 'winter':
    destination = 'Europe'
    place = 'Hotel'
    expenses = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{place} - {expenses:.2f}')