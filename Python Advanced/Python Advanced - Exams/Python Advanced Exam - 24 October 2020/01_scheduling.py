integers = list(map(int, input().split(", ")))

index = int(input())
cycles = 0
desired_integer = integers[index]

while desired_integer in integers:
    cycles += min(integers)
    integers.remove(min(integers))

print(cycles)
