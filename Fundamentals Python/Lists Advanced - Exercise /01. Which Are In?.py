subwords = input().split(', ')
words = input().split(', ')

new_list = []

for substr in subwords:
    for word in words:
        found_word = substr in word
        if found_word:
            new_list.append(substr)
            break

print(new_list)