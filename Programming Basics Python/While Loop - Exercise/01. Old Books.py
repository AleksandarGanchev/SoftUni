desired_book = input()
book = ''
book_count = 0

while desired_book != book:
    book = input()

    if desired_book != book and book != 'No More Books':
        book_count += 1

    elif book == 'No More Books':
        break

if desired_book == book:
    print(f"You checked {book_count} books and found it.")

elif desired_book != book:
    print("The book you search is not here!")