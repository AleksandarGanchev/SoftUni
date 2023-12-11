cards = input().split()

team_A_sent_off_players = []
team_B_sent_off_players = []


for card in  cards:
    if card in team_A_sent_off_players or card in team_B_sent_off_players:
        continue
    card_args = card.split('-')
    team_name = card_args[0]
    player_number = card_args[1]
    if team_name == 'A':
       team_A_sent_off_players.append(card)
    if team_name == 'B':
       team_B_sent_off_players.append(card)

    if len(team_A_sent_off_players) > 5 or len(team_B_sent_off_players) > 5:
        break

    team_A_left_players = 11 - len(team_A_sent_off_players)
    team_B_left_players = 11 - len(team_B_sent_off_players)

print(f"Team A - {team_A_left_players}; Team B - {team_B_left_players}")
if team_A_left_players < 7 or team_B_left_players < 7:
    print("Game was terminated")