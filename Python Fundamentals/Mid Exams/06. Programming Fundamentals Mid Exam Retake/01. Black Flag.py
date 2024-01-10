days = int(input())
plunder_for_day = int(input())
expected_plunder = int(input())
third_day = plunder_for_day / 2
total_plunder = 0

for index in range(1,days+1):
    if index % 3 == 0:
        total_plunder += plunder_for_day + plunder_for_day * 0.5
    else:
        total_plunder += plunder_for_day


    if index % 5 == 0:
        total_plunder *= 0.7


if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")

else:
    percentage = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")