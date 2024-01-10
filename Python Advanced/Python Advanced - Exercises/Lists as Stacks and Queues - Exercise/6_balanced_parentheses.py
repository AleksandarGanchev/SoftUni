from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    current_parentheses = parentheses.popleft()

    if current_parentheses in "{[(":
        open_parentheses.append(current_parentheses)
    elif not open_parentheses:
        print("NO")
        break
    else:
        if f"{open_parentheses.pop() + current_parentheses}" not in "{}[]()":
            print("NO")
            break

else:
    print("YES")









# from collections import deque
#
# stack = deque([])
# parentheses = input()
#
# all_matched = True
# for element in parentheses:
#     if element in "{[(":
#         stack.append(element)
#
#     elif "{[(" in stack:
#         if element == "}" and stack[-1] == "{":
#             stack.pop()
#         elif element == "]" and stack[-1] == "[":
#             stack.pop()
#         elif element == ")" and stack[-1] == "(":
#             stack.pop()
#         else:
#             all_matched = False
#             print("NO")
#             break
#
#     else:
#         all_matched = False
#         print("NO")
#         break
#
# if all_matched:
#     print("YES")
