from math import floor


tournaments = int(input())
points = int(input())
earned_points = 0
won_tournaments = 0

for i in range(tournaments):
    tournament_stage = input()
    if tournament_stage == 'W':
        earned_points += 2000
        won_tournaments += 1

    elif tournament_stage == 'F':
        earned_points += 1200

    elif tournament_stage == 'SF':
        earned_points += 720


average_points = earned_points / tournaments
won_percentage = won_tournaments / tournaments * 100

print(f"Final points: {floor(points+earned_points)}")
print(f"Average points: {floor(average_points)}")
print(f"{won_percentage:.2f}%")