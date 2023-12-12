electrons = int(input())
filled_shells = []

for el in range(1,electrons + 1 ):
    shell = 2 * (el ** 2)

    if shell >= electrons:
        filled_shells.append(electrons)
        break
    elif electrons > shell:
        filled_shells.append(shell)
    electrons -= shell

print(filled_shells)
