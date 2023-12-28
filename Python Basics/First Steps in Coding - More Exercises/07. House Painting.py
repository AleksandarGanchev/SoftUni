house_height = float(input())
house_length = float(input())
roof_height = float(input())


windows_area = 2.25
door_area = 2.4
green_paint = 3.4
red_paint = 4.3

side_wall = house_height * house_length
side_wall_total = (side_wall * 2) - (windows_area * 2)
back_wall = ((house_height * house_height) * 2) - door_area
total_area_walls = side_wall_total + back_wall
green_paint_needed = total_area_walls / green_paint


two_rectangle_roof = 2 * (house_height * house_length)
two_triangle_roof = 2 * (house_height * roof_height / 2)
total_area_roof = two_rectangle_roof + two_triangle_roof
red_paint_needed = total_area_roof / red_paint


print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")