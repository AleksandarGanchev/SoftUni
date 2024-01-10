cells = input().split('#')
water = int(input())
shutdown_cells = []
total_fire = 0
for cell in cells:
    cell_args =cell.split(' = ')
    level = cell_args[0]
    value = int(cell_args[1])

    if level == 'High' and (value < 81 or value > 125):
        continue

    if level == 'Medium' and (value < 51 or value > 80):
        continue

    if level == 'Low' and  (value < 1 or value > 50):
        continue

    if value > water:
        continue

    water -= value
    total_fire += value
    shutdown_cells.append(value)

effort = total_fire * 0.25

print('Cells:')
for cells_number in shutdown_cells:
    print(f' - {cells_number}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')