from collections import deque
from math import floor

string = deque(input().split())

index = 0
while index < len(string):
    element = string[index]

    if element == "*":
        for _ in range(index - 1):
            string.appendleft(int(string.popleft()) * int(string.popleft()))
    elif element == "/":
        for _ in range(index - 1):
            string.appendleft(int(string.popleft()) / int(string.popleft()))
    elif element == "+":
        for _ in range(index - 1):
            string.appendleft(int(string.popleft()) + int(string.popleft()))
    elif element == "-":
        for _ in range(index - 1):
            string.appendleft(int(string.popleft()) - int(string.popleft()))

    if element in "+-*/":
        del string[1]
        index = 1

    index += 1

print(floor(int(string[0])))
