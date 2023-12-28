n = int(input())

sum_people = 0
Musala = 0
Monblan = 0
Kilimandjaro = 0
K2 = 0
Everest = 0

for i in range (n):
    people_in_group = int(input())
    sum_people += people_in_group
    if people_in_group <= 5:
        Musala += people_in_group
    elif 6 <= people_in_group <= 12:
        Monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        Kilimandjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        K2 += people_in_group
    elif people_in_group >= 41:
        Everest += people_in_group

climbing_Musala = Musala/sum_people * 100
climbing_Monblan = Monblan/sum_people * 100
climbing_Kilimandjaro = Kilimandjaro/sum_people * 100
climbing_K2 = K2/sum_people * 100
climbing_Everest = Everest/sum_people * 100

print(f'{climbing_Musala:.2f}%')
print(f'{climbing_Monblan:.2f}%')
print(f'{climbing_Kilimandjaro:.2f}%')
print(f'{climbing_K2:.2f}%')
print(f'{climbing_Everest:.2f}%')