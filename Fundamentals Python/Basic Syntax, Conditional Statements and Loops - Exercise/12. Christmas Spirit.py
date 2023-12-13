quantity_of_decorations = int(input())
days_to_xmas = int(input())

total_cost = 0
points = 0
shopping_day = 0
while days_to_xmas > 0:
    shopping_day += 1
    if shopping_day % 11 == 0:
        quantity_of_decorations += 2
    if shopping_day % 2 == 0:
        total_cost += quantity_of_decorations * 2
        points += 5

    if shopping_day % 3 == 0:
        total_cost += quantity_of_decorations * 8
        points += 13

    if shopping_day % 5 == 0:
        total_cost += quantity_of_decorations * 15
        points += 17

    if shopping_day % 3 == 0 and shopping_day % 5 == 0:
        points += 30

    if shopping_day % 10 == 0:
        points -= 20
        total_cost += 23

    days_to_xmas -= 1

    if days_to_xmas == 0 and shopping_day % 10 == 0:
        points -= 30


print(f"Total cost: {total_cost}")
print(f"Total spirit: {points}")


