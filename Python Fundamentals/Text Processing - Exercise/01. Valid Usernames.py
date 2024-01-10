usernames = input().split(", ")


def right_length(user):
    if 3 <= len(user) <= 16:
        return True
    return False


def allowed_characters(user):
    for character in user:
        if not character.isalnum() and (character != "-" and character != "_"):
            return False
    return True


def has_redundant(user):
    if " " not in user:
        return True
    return False


def is_valid(users):
    for user in users:
        if right_length(user) and allowed_characters(user) and has_redundant(user) is True:
            print(user)


is_valid(usernames)






# data = input().split(', ')
# allowed_symbols = '-', '_'
#
# for username in data:
#     if len(username) < 3 or len(username) > 16:
#         continue
#     flag = True
#     for letter in username:
#         if letter.isdigit() or letter.isalpha() or letter in allowed_symbols:
#             pass
#         else:
#             flag = False
#     if flag:
#         print(username)
