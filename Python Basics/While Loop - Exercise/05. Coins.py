change = float(input())
coins_count = 0

while change > 0:
    if change >= 2:
        change -= 2
       # coins_count += 1
    elif change >= 1:
        change -= 1
        #coins_count += 1
    elif change >= 0.50:
        change -= 0.50
       # coins_count += 1
    elif change >= 0.20:
        change -= 0.20
        #coins_count += 1
    elif change >= 0.10:
        change -= 0.10
       # coins_count += 1
    elif change >= 0.05:
        change -= 0.05
       # coins_count += 1
    elif change >= 0.02:
        change -= 0.02
        #coins_count += 1
    elif change >= 0.01:
        change -= 0.01
        #coins_count += 1

    change = round(change, 2)
    coins_count += 1
print(round(coins_count))