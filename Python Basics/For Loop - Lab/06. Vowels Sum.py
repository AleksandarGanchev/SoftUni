text = input()
summary  = 0

for i in range (0,len(text)):
    if text[i] == 'a':
        summary += 1
    elif text[i] == 'e':
        summary += 2
    elif text[i] == 'i':
        summary += 3
    elif text[i] == 'o':
        summary += 4
    elif text[i] == 'u':
        summary += 5


print(summary)