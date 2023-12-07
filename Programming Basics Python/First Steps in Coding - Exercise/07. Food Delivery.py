count_chicken_menu = int(input())
count_fish_menu = int(input())
count_veggie_menu = int(input())

delivery_price = 2.50

chicken_menu = count_chicken_menu * 10.35
fish_menu = count_fish_menu * 12.40
veggie_menu = count_veggie_menu * 8.15

total_price = chicken_menu + fish_menu + veggie_menu
dessert = total_price * 0.2

final_price = total_price + dessert + delivery_price
print(final_price)