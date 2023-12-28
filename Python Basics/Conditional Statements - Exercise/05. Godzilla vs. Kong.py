budget =  float(input())
statist = int(input())
clothes_price = float(input())

dekor = budget * 0.10

if statist > 150:
    clothes_price = clothes_price - clothes_price * 0.10


total = abs(budget - (statist * clothes_price +dekor))
spendings = statist * clothes_price + dekor

if spendings > budget:
    print('Not enough money!')
    print(f'Wingard needs {total:.2f} leva more.')

else:
    print('Action!')
    print(f'Wingard starts filming with {total:.2f} leva left. ')