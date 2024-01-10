phonebook = {}
data = input()
while "-" in data:
    name, phone_number = data.split("-")
    phonebook[name] = phone_number
    data = input()

n = int(data)
for _ in range(n):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
