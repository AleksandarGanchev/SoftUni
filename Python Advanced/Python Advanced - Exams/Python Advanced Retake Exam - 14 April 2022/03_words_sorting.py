def words_sorting(*args):
    dictionary = {}
    for word in args:
        dictionary[word] = 0
        for letter in word:
            dictionary[word] += ord(letter)

    sum_values = sum(dictionary.values())

    output = ''
    if sum_values % 2 == 0:
        sorted_result = sorted(dictionary.items(), key=lambda x: (x[0], x[1]))
    else:
        sorted_result = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))

    for key, value in sorted_result:
        output += f"{key} - {value}"'\n'

    return output
