student_tickets = 0
standard_tickets = 0
kid_tickets = 0
tickets_per_movie = 0
sold_seats = 0
percentage_per_movie = 0



movie_name = input()
while movie_name != 'Finish':
    free_seats = int(input())
    sold_seats = 0



    while free_seats > 0:
        ticket_type = input()
        if ticket_type == 'End':

            break
        free_seats -= 1
        sold_seats += 1


        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1


    percentage_per_movie = sold_seats / (sold_seats + free_seats) * 100
    print(f'{movie_name} - {percentage_per_movie:.2f}% full.')
    movie_name = input()

total_tickets = standard_tickets + student_tickets + kid_tickets
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets/total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets/total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets/total_tickets * 100:.2f}% kids tickets.")