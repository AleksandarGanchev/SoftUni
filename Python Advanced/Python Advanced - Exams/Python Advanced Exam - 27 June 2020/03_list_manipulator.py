def list_manipulator(numbers, *args):
    if args[0] == "add":
        if args[1] == "beginning":
            result = []
            nums = args[2:]
            for num in nums:
                result.append(num)

            result.extend(numbers)
            return result

        elif args[1] == "end":
            nums = args[2:]
            for num in nums:
                numbers.append(num)

            return numbers

    elif args[0] == "remove":
        if args[1] == "beginning":
            try:
                numbers = numbers[args[2]::]
            except IndexError:
                numbers = numbers[1::]

        elif args[1] == "end":
            try:
                test = args[2]
                for i in range(test):
                    numbers.pop()
            except IndexError:
                numbers.pop()

        return numbers
