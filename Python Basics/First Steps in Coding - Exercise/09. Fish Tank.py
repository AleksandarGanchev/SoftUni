length = int(input())
width = int(input())
height = int(input())
percent = float(input())


volume = length * width * height
total_volume = volume / 1000
taken_place = percent / 100
needed_water = total_volume * (1- taken_place)
print(needed_water)