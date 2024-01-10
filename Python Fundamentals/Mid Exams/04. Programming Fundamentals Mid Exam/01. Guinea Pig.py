quantity_food = float(input()) * 1000
quantity_hay= float(input()) * 1000
quantity_cover = float(input()) * 1000
guineas_weight = float(input()) * 1000

flag = True
counter = 0
while counter < 30:
    counter += 1
    quantity_food -= 300
    if counter % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if counter % 3 == 0:
        quantity_cover -= 1/3 * guineas_weight

    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        print("Merry must go to the pet store!")
        flag = False
        break

if flag:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food/1000:.2f}, Hay: {quantity_hay/1000:.2f}, Cover: {quantity_cover/1000:.2f}.")
