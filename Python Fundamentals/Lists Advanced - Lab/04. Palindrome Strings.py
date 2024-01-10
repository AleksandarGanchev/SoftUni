words = input().split()
palindrome_word = input()
counter = 0
new_list = []

for word in words:
    reversed_word = word[::-1]
    if word == reversed_word:
        new_list.append(word)
        if word == palindrome_word:
            counter += 1


print(new_list)
print(f"Found palindrome {counter} times")