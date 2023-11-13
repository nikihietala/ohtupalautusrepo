import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team:5} {self.goals} + {self.assists} = {self.points}"

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()
    
    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(player_dict) for player_dict in response]

class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.players
    
    def top_scorers_by_nationality(self, nationality):
        players_of_x_nation = [player for player in self.players if player.nationality == nationality]
        return sorted(players_of_x_nation, key=lambda player: player.points, reverse=True)
