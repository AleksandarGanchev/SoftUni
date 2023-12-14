import re
pattern = r'@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@\#{1,}'

result = []
n = int(input())
for barcode in range(n):
    data = input()
    match = re.findall(pattern, data)
    if match:
        for item in match:
            for digit in item:
                if digit.isdigit():
                    result.append(digit)
            if result:
                result = (''.join(result))
                print(f"Product group: {result}")

            else:
                print('Product group: 00')

        result = []
    else:
        print("Invalid barcode")
