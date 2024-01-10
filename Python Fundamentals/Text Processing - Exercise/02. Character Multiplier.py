data = input().split(' ')
first = data[0]
second = data [1]
result = 0
first_length = len(first)
second_length = len(second)

if first_length <= second_length:
    for index in range(first_length):
        first_letter = first[index]
        second_letter = second[index]
        result += ord(first_letter) * ord(second_letter)

    for index in range(first_length,second_length):
        result += ord(second[index])

elif first_length > second_length:
    for index in range(second_length):
        first_letter = first[index]
        second_letter = second[index]
        result += ord(first_letter) * ord(second_letter)

    for index in range(second_length, first_length):
        result += ord(first[index])

print(result)