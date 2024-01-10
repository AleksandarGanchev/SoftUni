n = int(input())
word = input()
all_strings = []
strings_with_word = []

for i in range(n):
    command = input()
    all_strings.append(command)
    if word in command:
        strings_with_word.append(command)

print(all_strings)
print(strings_with_word)