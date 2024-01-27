def team_lineup(*args):
    line_up = {}
    for player, country in args:
        if country not in line_up:
            line_up[country] = [player]
        else:
            line_up[country].append(player)

    result = dict(sorted(line_up.items(), key=lambda x: (-len(x[1]), (x[0]))))

    output = ''
    for country, player_names in result.items():
        output += f'{country}:\n'

        for player in player_names:
            output += f"  -{player}\n"

    return output


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
