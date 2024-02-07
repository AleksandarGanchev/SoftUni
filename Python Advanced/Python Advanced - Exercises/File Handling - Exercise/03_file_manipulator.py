import os

command = input()
while command != "End":
    action, *info = command.split("-")
    if action == "Create":
        file_name = info[0]
        with open(file_name, "w"):
            pass

    elif action == "Add":
        file_name, content = info[0], info[1]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif action == "Replace":
        file_name, old_string, new_string = info[0], info[1], info[2]
        try:
            with open(file_name, "r+") as file:
                text = file.read()
                text = text.replace(old_string, new_string)

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        file_name = info[0]
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command = input()
