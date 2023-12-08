actor_name = input()
points = float(input())
n = int(input())

nomination_points = 1250.5

for i in range (n):
    judge_name = input()
    judge_points = float(input())
    points += len(judge_name) * judge_points / 2

    if points > nomination_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break


if points <= nomination_points:
    print(f"Sorry, {actor_name} you need {nomination_points-points:.1f} more!")