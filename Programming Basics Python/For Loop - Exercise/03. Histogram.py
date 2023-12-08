n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0



for _ in range (n):
    number = int(input())
    if number < 200:
        p1_count += 1
    elif 200 <= number <= 399:
        p2_count += 1
    elif 400 <= number <= 599:
        p3_count += 1
    elif 600 <= number <= 799:
        p4_count += 1
    elif number >= 800:
        p5_count += 1


p1_percentage = p1_count / n * 100
p2_percentage = p2_count / n * 100
p3_percentage = p3_count / n * 100
p4_percentage = p4_count / n * 100
p5_percentage = p5_count / n * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')
