force_book = {}

command = input()
while command != "Lumpawaroo":
    if "|" in command:
        side, user = command.split(" | ")
        user_not_found = True
        for value in force_book.values():
            if user in value:
                user_not_found = False
                break
        if user_not_found:
            if side not in force_book:
                force_book[side] = [user]
            else:
                force_book[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")
        for value in force_book.values():
            if user in value:
                value.remove(user)
                break

        force_user_not_found = True
        for force_users in force_book.values():
            if user in force_users:
                force_user_not_found = False
                break

        if force_user_not_found:
            if side not in force_book:
                force_book[side] = [user]
            else:
                force_book[side].append(user)
            print(f"{user} joins the {side} side!")

    command = input()

for force_side, force_users in force_book.items():
    if len(force_users):
        print(f"Side: {force_side}, Members: {len(force_users)}")
    for force_user in force_users:
        print(f"! {force_user}")
