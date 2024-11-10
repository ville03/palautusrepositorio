"""moi"""
class Player:
    """moi"""
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.country = dictionary['nationality']
        self.team = dictionary['team']
        self.goals = dictionary['goals']
        self.assists = dictionary['assists']
        self.total=self.goals+self.assists

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.total}"
