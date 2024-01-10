numbers =[int(x) for x in input().split(', ')]
beggers_number = int(input())

each_begger = [0] * beggers_number

for index in range(len(numbers)):
    beggar_index = index % beggers_number
    number = (numbers[index])
    each_begger[beggar_index] += number

print(each_begger)