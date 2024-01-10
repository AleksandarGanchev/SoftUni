first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command
    if command == "Add First":
        [first_sequence.add(int(num)) for num in data]
    elif command == "Add Second":
        [second_sequence.add(int(num)) for num in data]
    elif command == "Remove First":
        [first_sequence.discard(int(num)) for num in data]
    elif command == "Remove Second":
        [second_sequence.discard(int(num)) for num in data]
    elif command == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
