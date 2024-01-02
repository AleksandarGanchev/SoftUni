number_of_guests = int(input())

invited_guests = set()
for _ in range(number_of_guests):
    guest_reservation_number = input()
    invited_guests.add(guest_reservation_number)

coming_guests = input()
while coming_guests != "END":
    invited_guests.remove(coming_guests)

    coming_guests = input()

print(len(invited_guests))
for guest_num in sorted(invited_guests):
    print(guest_num)
