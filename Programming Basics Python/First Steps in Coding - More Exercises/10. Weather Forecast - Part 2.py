degrees = float(input())

if 35.00 < degrees or degrees <= 5.00:
    print("unknown")
elif 5.00 <= degrees <= 11.9:
    print("Cold")
elif degrees <= 14.90:
    print("Cool")
elif degrees <= 20.00:
    print("Mild")
elif degrees <= 25.90:
    print("Warm")
elif degrees <= 35.00:
    print("Hot")