from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        if sort_by == SortBy.POINTS:
            sort_by_points = lambda player: player.points
        elif sort_by == SortBy.GOALS:
            sort_by_points = lambda player: player.goals
        elif sort_by == SortBy.ASSISTS:
            sort_by_points = lambda player: player.assists
        else:
            raise Exception("Invalid sort_by value")

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        return sorted_players[:how_many]
