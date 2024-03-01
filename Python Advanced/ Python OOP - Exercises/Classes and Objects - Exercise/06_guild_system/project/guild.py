from project import Player



class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        players_to_remove = [p for p in self.players if p.name == player_name]

        if not players_to_remove:
            return f"Player {player_name} is not in the guild."

        player = players_to_remove[0]
        self.players.remove(player)
        player.guild = Player.DEFAULT_GUILD

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = '\n'.join([p.player_info() for p in self.players])
        return f"Guild: {self.name}\n" + \
               f"{players_info}"
