class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    MIN_WINNING_SCORE = 4
    SCORE_DIFF_FOR_WIN = 2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.is_tie():
            return self.score_when_tie()
        if self.is_late_game():
            return self.score_in_late_game()
        return self.normal_scoring()

    def is_tie(self):
        return self.m_score1 == self.m_score2

    def score_when_tie(self):
        if self.m_score1 < 3:
            return f"{self.SCORE_NAMES[self.m_score1]}-All"
        return "Deuce"

    def is_late_game(self):
        return self.m_score1 >= self.MIN_WINNING_SCORE or self.m_score2 >= self.MIN_WINNING_SCORE

    def score_in_late_game(self):
        score_difference = self.m_score1 - self.m_score2
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= self.SCORE_DIFF_FOR_WIN:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def normal_scoring(self):
        return f"{self.SCORE_NAMES[self.m_score1]}-{self.SCORE_NAMES[self.m_score2]}"
