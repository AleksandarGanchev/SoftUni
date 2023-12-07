month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
total_studio = 0
total_apartment = 0


if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 < nights <= 14:
        studio_price = studio_price - studio_price * 0.05
    if nights > 14:
        studio_price = studio_price - studio_price * 0.3


if month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14 and month == 'June' or  month == 'September':
        studio_price = studio_price - studio_price * 0.2

elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77


if nights > 14:
    apartment_price = apartment_price - apartment_price * 0.10

total_studio = nights * studio_price
total_apartment = nights * apartment_price

print(f'Apartment: {total_apartment:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')