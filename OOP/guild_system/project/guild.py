from project.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        try:
            kicked = next(filter(lambda k: k.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(kicked)
        kicked.guild = 'Unaffiliated'
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = ''

        result += f"Guild: {self.name}\n"
        result += '\n'.join(p.player_info() for p in self.players)

        return result


player = Player("George", 50, 100)

print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 30))
print(player.player_info())
guild = Guild("UGT")

print(guild.assign_player(player))

print(guild.guild_info())
