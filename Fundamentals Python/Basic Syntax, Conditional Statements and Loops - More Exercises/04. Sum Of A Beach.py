def occurrences(string):
    counter = 0
    substrings = "sand", "water", "fish", "sun"
    counter += string.count("sand")
    counter += string.count("water")
    counter += string.count("fish")
    counter += string.count("sun")
    return counter


string = input().lower()
print(occurrences(string))



# string = input().lower()
# substrings = "sand", "water", "fish", "sun"
#
# occurrences = 0
# occurrences += string.count("sand")
# occurrences += string.count("water")
# occurrences += string.count("fish")
# occurrences += string.count("sun")
#
# print(occurrences)