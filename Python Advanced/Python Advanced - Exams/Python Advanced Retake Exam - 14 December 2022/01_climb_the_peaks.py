from collections import deque

food_portions = [int(x) for x in input().split(", ")]
staminas = deque(int(x) for x in input().split(", "))

peak_values = [80, 90, 100, 60, 70]
peak_names = ["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"]
climbed_peaks = []

days = 0
while days <= 7:
    if food_portions and staminas:
        level = food_portions.pop() + staminas.popleft()
        if peak_values:
            if level >= peak_values[0]:
                climbed_peaks.append(peak_names[0])
                peak_names.pop(0)
                peak_values.pop(0)
        else:
            break
    else:
        break

    days += 1

if len(climbed_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print("Conquered peaks:")
    for peak in climbed_peaks:
        print(peak)
