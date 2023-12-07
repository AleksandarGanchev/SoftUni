from math import floor

count_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_day = count_pages / pages_per_hour / days
print(floor(hours_per_day))
