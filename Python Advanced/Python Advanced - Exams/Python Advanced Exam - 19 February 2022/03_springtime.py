def start_spring(**kwargs):
    springtime = {}
    for spring_object, spring_type in kwargs.items():
        if spring_type not in springtime:
            springtime[spring_type] = []
        springtime[spring_type].append(spring_object)

    sorted_elements = sorted(springtime.items(), key=lambda x: (-len(x[1]), x[0]))

    output = ""
    for name, kinds in sorted_elements:
        output += f"{name}:\n"
        for kind in sorted(kinds):
            output += f"-{kind}\n"

    return output
