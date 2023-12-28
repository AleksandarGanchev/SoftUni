holiday_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minion_count = int(input())
trucks_count = int(input())

total = puzzles_count * 2.60 + talking_dolls_count * 3 + teddy_bears_count * 4.10 + minion_count * 8.20 + trucks_count * 2
total = total - total * 0.10

if puzzles_count + talking_dolls_count + teddy_bears_count + minion_count + trucks_count >= 50:
    total = total - total * 0.25

diff = (total - holiday_price)

if diff >= 0 :
    print(f'Yes! {diff:.2f} lv left.')


else:
    print(f'Not enough money! {abs(diff):.2f} lv needed.')