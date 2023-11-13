import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(player_dict)
            players.append(player)

    players_by_points = sorted(players, key=lambda player: player.points, reverse=True)

    print("Players from FIN")

    for player in players_by_points:
        print(player)

if __name__ == "__main__":
    main()