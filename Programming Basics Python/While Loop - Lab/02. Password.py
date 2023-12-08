username = input()
password = input()

try_password = input()

while password != try_password:
    try_password = input()

if password == try_password:
    print(f"Welcome {username}!")