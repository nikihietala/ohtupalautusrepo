import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_returns_correct_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
    
    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Kurrixxx")

        self.assertEqual(player, None)
    
    def test_team_returns_all_players_of_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
    
    def test_team_returns_empty_list_if_no_players_found(self):
        players = self.stats.team("ANA")

        self.assertEqual(len(players), 0)
    
    def test_top_returns_top_scorers(self):
        top_scorers = self.stats.top(3)

        self.assertEqual(len(top_scorers), 3)
        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Lemieux")
        self.assertEqual(top_scorers[2].name, "Yzerman")
    
