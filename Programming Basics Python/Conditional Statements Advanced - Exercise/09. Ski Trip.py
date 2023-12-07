days = int(input())
days -= 1
room_type = input()
rating = input()
price = 0


if room_type == 'room for one person' and rating == 'positive':
    price = 18 + 18 * 0.25
if room_type == 'room for one person' and rating == 'negative':
    price = 18 + 18 * 0.1


if room_type == 'apartment' and days < 10:
    price = 25 - 25 * 0.3
if room_type == 'apartment' and 10 <= days <= 15:
    price = 25 - 25 * 0.35
if room_type == 'apartment' and days > 15:
    price = 25 - 25 * 0.5
if room_type == 'apartment' and rating == 'positive':
    price = price + price * 0.25
if room_type == 'apartment' and rating == 'negative':
    price = price - price * 0.1

if room_type == 'president apartment' and days < 10:
    price = 35 - 35 * 0.1
if room_type == 'president apartment' and 10 <= days <= 15:
    price = 35 - 35 * 0.15
if room_type == 'president apartment' and days > 15:
    price = 35 - 35 * 0.2
if room_type == 'president apartment' and rating == 'positive':
    price = price + price * 0.25
if room_type == 'president apartment' and rating == 'negative':
    price = price - price * 0.1

total_president = days * price
total_one_person = days * price
total_apartment = days * price

if room_type == 'room for one person':
    print(f'{total_one_person:.2f}')
if room_type == 'apartment':
    print(f'{total_apartment:.2f}')
if room_type == 'president apartment':
    print(f'{total_president:.2f}')