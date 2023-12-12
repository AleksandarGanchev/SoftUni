words = input().split()
result = []

for word in words:
    cur_word = list(word)

    char_code = []
    while cur_word[0].isdigit():
        char_code.append(cur_word.pop(0))

    cur_word.insert(0, chr(int("".join(char_code))))
    cur_word[1], cur_word[-1] = cur_word[-1], cur_word[1]

    result.append("".join(cur_word))

print(" ".join(result))