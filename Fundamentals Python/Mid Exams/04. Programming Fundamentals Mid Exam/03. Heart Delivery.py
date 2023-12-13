neighborhood = [int(x) for x in input().split('@')]

index = 0
command = input()
while command != 'Love!':

    command_args = command.split()
    jump = command_args[0]
    length = int(command_args[1])
    index += length

    if index + 1  > len(neighborhood):
        index = 0

    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f"Place {index} has Valentine's day." )

    command = input()

counter = 0
for house in neighborhood:
    if house != 0:
        counter += 1

print(f"Cupid's last position was {index}.")
if counter == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")
