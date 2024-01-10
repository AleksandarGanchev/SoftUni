factor = int(input())
count = int(input())

list = []

for i in range(1,count+1):
    number = factor * i
    list.append(number)

print(list)
