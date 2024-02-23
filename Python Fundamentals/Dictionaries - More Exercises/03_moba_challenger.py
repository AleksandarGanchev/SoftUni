command = input()
statistics = {}
while command != "Season end":
    if '->' in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)
        if player not in statistics:
            statistics[player] = {}
        if position not in statistics[player]:
            statistics[player][position] = skill
        else:
            if skill > statistics[player][position]:
                statistics[player][position] = skill

    elif "vs" in command:
        first_player, second_player = command.split(' vs ')
        if first_player in statistics and second_player in statistics:
            common_positions = set(statistics[first_player].keys()) & set(statistics[second_player].keys())

            if common_positions:
                total_skill_first = sum(statistics[first_player][pos] for pos in common_positions)
                total_skill_second = sum(statistics[second_player][pos] for pos in common_positions)

                if total_skill_first > total_skill_second:
                    del statistics[second_player]
                elif total_skill_first < total_skill_second:
                    del statistics[first_player]

    command = input()

sorted_skills = dict(sorted(statistics.items(), key=lambda x: (-sum(x[1].values()), x[0])))

for player, info in sorted_skills.items():
    print(f"{player}: {sum(info.values())} skill")
    sorted_names = dict(sorted(info.items(), key=lambda x: (-x[1], x[0])))
    for position, skill in sorted_names.items():
        print(f"- {position} <::> {skill}")
