from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

found_flower = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower in flowers.keys():
        flowers[flower] = flowers[flower].replace(vowel, '')
        flowers[flower] = flowers[flower].replace(consonant, '')

        if flowers[flower] == '':
            print(f"Word found: {flower}")
            found_flower = True
            break

    if found_flower:
        break

else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
