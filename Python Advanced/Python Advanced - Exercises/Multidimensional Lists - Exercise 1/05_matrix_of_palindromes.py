i, j = [int(x) for x in input().split()]

start_char = 97
for r in range(i):
    for c in range(j):
        print(f"{chr(97+r)}{chr(97+r+c)}{chr(97+r)}", end=" ")

    print()