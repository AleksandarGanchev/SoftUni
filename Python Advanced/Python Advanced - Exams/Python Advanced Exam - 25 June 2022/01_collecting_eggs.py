from collections import deque

eggs_size = deque(int(x) for x in input().split(", "))
papers_size = deque(int(x) for x in input().split(", "))

boxes = 0
while eggs_size and papers_size:

    egg_size = eggs_size.popleft()
    if egg_size <= 0:
        continue

    if egg_size == 13:
        first_egg = papers_size.popleft()
        last_egg = papers_size.pop()

        papers_size.appendleft(last_egg)
        papers_size.append(first_egg)

        continue

    paper_size = papers_size.pop()

    if egg_size + paper_size <= 50:
        boxes += 1


if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_size])}")
elif papers_size:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers_size])}")
