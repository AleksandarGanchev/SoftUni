numbers = input().split()
string = input()

message = ""
for num in numbers:
    desired_index = sum([int(x) for x in num])
    if desired_index >= len(string):
        desired_index = desired_index - len(string)
    message += string[desired_index]
    string = string[:desired_index] + string[desired_index + 1:]

print(message)





