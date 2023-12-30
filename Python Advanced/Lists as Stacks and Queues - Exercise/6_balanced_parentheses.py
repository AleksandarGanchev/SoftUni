from collections import deque

stack = deque([])
parentheses = input()

all_matched = True
for element in parentheses:
    if element == "{" or element == "[" or element == "(":
        stack.append(element)

    elif "{" in stack or "[" in stack or "(" in stack:
        if element == "}" and stack[-1] == "{":
            stack.pop()
        elif element == "]" and stack[-1] == "[":
            stack.pop()
        elif element == ")" and stack[-1] == "(":
            stack.pop()
        else:
            all_matched = False
            print("NO")
            break

    else:
        all_matched = False
        print("NO")
        break

if all_matched:
    print("YES")
