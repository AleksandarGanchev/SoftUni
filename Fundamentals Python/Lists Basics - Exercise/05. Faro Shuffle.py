cards = input().split()
shuffles = int(input())

middle = len(cards) // 2 - 1

shuffled = cards[1:-1]
for i in range(shuffles):
    first_part = shuffled[:middle]
    second_part = shuffled[middle:]

#  b c d           e f g
    new_deck = []
    for index in range(len(first_part)):
        new_deck.append(second_part[index])
        new_deck.append(first_part[index])

        shuffled = new_deck

first= [cards[0]]
last = [cards[-1]]


print(first+shuffled+last)
