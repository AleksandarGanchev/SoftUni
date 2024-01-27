def softuni_students(*args, **kwargs):
    output = []
    invalid_usernames = []

    for course, username in args:
        for course_id, course_name in kwargs.items():
            if course == course_id:
                output.append(f"*** A student with the username {username} has successfully finished the course {course_name}!")
            if course not in kwargs.keys() and username not in invalid_usernames:
                invalid_usernames.append(username)

    output = sorted(output)

    if invalid_usernames:
        invalid_username_result = f"!!! Invalid course students: {', '.join(sorted(invalid_usernames))}"
        output.append(invalid_username_result)

    return "\n".join(output)



print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))

