string = input()
result = ""

explosion_strength = 0
for index in range(len(string)):
    if string[index] == ">":
        explosion_strength += int(string[index+1])
        result += string[index]
    elif explosion_strength > 0 and string[index] != ">":
        explosion_strength -= 1
    else:
        result += string[index]

print(result)
