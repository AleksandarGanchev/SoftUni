from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = [int(x) for x in input().split()]

is_lost = True
while tools and len(substances) > 0:
    tool = tools.popleft()
    substance = substances.pop()

    result = tool * substance
    if result in challenges:
        challenges.remove(result)

    else:
        tools.append(tool+1)
        if substance - 1 > 0:
            substances.append(substance-1)

    if not len(challenges):
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        is_lost = False
        break

if is_lost:
    print("Harry is lost in the temple. Oblivion awaits him.")
if tools:
    print("Tools: ", end="")
    print(f"{', '.join([str(x) for x in tools])}")
if substances:
    print("Substances: ", end="")
    print(f"{', '.join([str(x) for x in substances])}")
if challenges:
    print("Challenges: ", end="")
    print(f"{', '.join([str(x) for x in challenges])}")
