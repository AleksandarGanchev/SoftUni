stack = []

n = int(input())
for _ in range(n):
    data = input().split()
    if data[0] == "1":
        stack.append(int(data[1]))
    elif stack:
        if data[0] == "2":
            stack.pop()
        elif data[0] == "3":
            print(max(stack))
        elif data[0] == "4":
            print(min(stack))

while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")
