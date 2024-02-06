def flights(*args):
    destination = ''
    result = {}
    for data in args:
        if data == "Finish":
            break
        if isinstance(data, str):
            destination = data
            if data not in result:
                result[data] = 0
        else:
            result[destination] += int(data)

    return result
