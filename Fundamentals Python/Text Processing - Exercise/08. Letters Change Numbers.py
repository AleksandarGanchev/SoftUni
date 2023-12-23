strings = input().split()
result = 0

for string in strings:
    current_number = ""
    for index in range(len(string)):
        if string[index].isdigit():
            current_number += string[index]

        else:
            if len(current_number) > 0:
                for idx in range(index, 0, -1):
                    if string[idx-1].isalpha():
                        if string[idx-1].isupper():
                            result += int(current_number) / (ord(string[idx-1].lower()) - 96)
                            break
                        else:
                            result += int(current_number) * (ord(string[idx-1].lower()) - 96)
                            break

                for next_index in range(index,len(string)):
                    if string[next_index].isalpha():
                        if string[next_index].isupper():


                            result -= ord(string[next_index].lower()) - 96
                        else:
                            result +=  ord(string[next_index].lower() ) - 96



    current_number = ""


print(f"{result:.2f}")