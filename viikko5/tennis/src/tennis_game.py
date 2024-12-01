class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_balls_won = 0
        self.player2_balls_won = 0

    def won_point(self, player):
        if player == "player1":
            self.player1_balls_won += 1
        else:
            self.player2_balls_won += 1

    def get_score(self):
        if self.player1_balls_won == self.player2_balls_won:
            if self.player1_balls_won == 0:
                return "Love-All"
            elif self.player1_balls_won == 1:
                return "Fifteen-All"
            elif self.player1_balls_won == 2:
                return "Thirty-All"
            else:
                return "Deuce"
            
        if self.player1_balls_won >= 4 or self.player2_balls_won >= 4:
            player1_advantage = self.player1_balls_won - self.player2_balls_won

            if player1_advantage >= 2:
                return "Win for player1"
            if player1_advantage == 1:
                return "Advantage player1"
            if player1_advantage == -1:
                return "Advantage player2"
            return "Win for player2"

        player1_score = ""
        player2_score = ""
    
        if self.player1_balls_won == 0:
            player1_score = "Love"
        elif self.player1_balls_won == 1:
            player1_score = "Fifteen"
        elif self.player1_balls_won == 2:
            player1_score = "Thirty"
        else:
            player1_score = "Forty"

        if self.player2_balls_won == 0:
            player2_score = "Love"
        elif self.player2_balls_won == 1:
            player2_score = "Fifteen"
        elif self.player2_balls_won == 2:
            player2_score = "Thirty"
        else:
            player2_score = "Forty"

        return player1_score + "-" + player2_score
