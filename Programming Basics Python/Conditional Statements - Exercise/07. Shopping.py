budget = float(input())
graphic_card_count = float(input())
cpu_count = float(input())
ram_count = float(input())

graphic_card_price = 250
cpu_price = (graphic_card_count * graphic_card_price) * 0.35
ram_price = (graphic_card_count * graphic_card_price) * 0.10


total_cpu = cpu_price * cpu_count
total_ram = ram_price  * ram_count
total_graphic = graphic_card_price * graphic_card_count

expenses = total_cpu + total_graphic + total_ram

final = expenses

if graphic_card_count > cpu_count:
   final = expenses - expenses * 0.15


if budget >= final:
    print(f' You have {budget-final:.2f} leva left!')

else:
    print(f'Not enough money! You need {abs(budget-final):.2f} leva more!')