expression = input()
stack = []
for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        end_index = index
        start_index = stack.pop()
        print(expression[start_index:end_index+1])
