years = int(input()) + 1

find_year = False

while not find_year:
    find_year = True
    for num in range(len(str(years))):
        if str(years).count(str(years)[num]) != 1:
            years = int(years) + 1
            find_year = False
            break

print(years)
