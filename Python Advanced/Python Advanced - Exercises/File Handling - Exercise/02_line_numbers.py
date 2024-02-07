from string import punctuation

with open("line_numbers_txt.txt", "r") as file:
    text = file.readlines()

output = open("output.txt", "w")

for row in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output.write(f"Line {row+1}: {''.join(text[row][:-1])} ({letters})({marks})\n")
