def function(animals):
    if animals[-1] == 'wolf':
        return "Please go away and stop eating my sheep"
    else:
        counter = 0
        for animal in reversed(animals):
            if animal == 'wolf':
                return f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!"
            counter += 1


animals = input().split(', ')
print(function(animals))


# animals = input().split(', ')
#
# if animals[-1] == 'wolf':
#     print("Please go away and stop eating my sheep")
# else:
#     counter = 0
#     for animal in reversed(animals):
#         if animal == 'wolf':
#             print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
#         counter += 1
