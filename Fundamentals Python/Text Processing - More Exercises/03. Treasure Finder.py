import re

keys = [int(x) for x in input().split()]
char = ""
material = ""
coordinates = ""

message = input()
while message != "find":
    decrypted_message = ""
    index = 0
    for element in message:
        if index < len(keys):
            char = chr(ord(element)-keys[index])
            decrypted_message += char
            index += 1
        else:
            decrypted_message += chr(ord(element) - keys[0])
            index = 1

    pattern = "&(?P<material>.+)&(?P<location>.+)<(?P<coordinates>.+)>"
    result = re.findall(pattern, decrypted_message)
    for match in result:
        material = match[0]
        coordinates = match[2]
        break

    print(f"Found {material} at {coordinates}")

    message = input()
