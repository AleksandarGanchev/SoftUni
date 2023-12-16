data = input().split()
dictionary = {}

for word in data:
    for letter in word:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

for letter, occurrences  in dictionary.items():
    print(f"{letter} -> {occurrences}")
