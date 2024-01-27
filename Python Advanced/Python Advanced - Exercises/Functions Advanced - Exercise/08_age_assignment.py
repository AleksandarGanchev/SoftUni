def age_assignment(*args, **kwargs):
    result = []

    for name in args:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")

    return '\n'.join(sorted(result))
