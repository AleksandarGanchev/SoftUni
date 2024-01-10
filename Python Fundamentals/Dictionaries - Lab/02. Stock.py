command = input().split()
dictionary = {}
products = input().split()

for i in range(0,len(command), 2):
    product = command[i]
    quantity = command[i+1]
    dictionary[product] = int(quantity)

for element in products:
    if element in dictionary:
        print(f"We have {dictionary[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")