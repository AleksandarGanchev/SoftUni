def loading_bar(integer):
    percent_count = int(number / 10)
    dots = (100 - number) // 10
    if percent_count == 10:
        return "100% Complete!\n" + "["+ percent_count * "%" + "]"
    else:
        return f"{number}" +"%"  +" " + "[" + percent_count * "%" + dots * "." + "]\n""Still loading..."


number = int(input())
print(loading_bar(number))

