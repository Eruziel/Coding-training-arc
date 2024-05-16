def team_lineup(*args):
    teams = {}
    result = ''
    for name, country in args:
        if country not in teams:
            teams[country] = []

        teams[country].append(name)

    sorted_teams = sorted(teams.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for country, players in sorted_teams:
        result += f"{country}:\n" + '\n'.join(f'  -{p}' for p in players) + '\n'

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


