destination = input()
min_budget = float(input())

savings = 0

while destination != 'End':

    if savings >= min_budget:
        print(f"Going to {destination}!")
        destination = input()
        if destination == 'End':
            break
        min_budget = float(input())
        savings = 0

    while min_budget > savings:
        savings += float(input())