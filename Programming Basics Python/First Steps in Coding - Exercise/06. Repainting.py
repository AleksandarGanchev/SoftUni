Required_amount_of_nylon = int(input())
Required_quantity_of_paint = int(input())
Quantity_of_thinner = int(input())
bags = 0.40
Hours_for_which_the_craftsmen_will_do_the_work = int(input())

nylon_sum = (Required_amount_of_nylon + 2) * 1.50
paint_sum = (Required_quantity_of_paint + (Required_quantity_of_paint * 0.10)) * 14.50
thinner_sum = Quantity_of_thinner * 5.00

all_materials = nylon_sum + paint_sum + thinner_sum + bags
amount_for_masters = (all_materials * 0.30) * Hours_for_which_the_craftsmen_will_do_the_work
the_sum_of_all_coast = all_materials + amount_for_masters

print(the_sum_of_all_coast)