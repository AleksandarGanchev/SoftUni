substring = input()
string = input()

flag = True
while flag:
    if substring in string:
        string = string.replace(substring, '')
    else:
        flag = False


print(string)