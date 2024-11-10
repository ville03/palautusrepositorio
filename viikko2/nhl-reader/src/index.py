"""moi"""
import requests
from player import Player

def main():
    """moi"""
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

class PlayerReader():
    """moi"""
    def __init__(self,url):
        self.url=url

    def get_players(self):
        """moi"""
        lista = requests.get(self.url, timeout=60).json()
        players=[]
        for player_dict in lista:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats():
    """moi"""
    def __init__(self,reader):
        self.reader=reader

    def top_scorers_by_nationality(self,nationality):
        """moi"""
        lista=[]
        players=self.reader.get_players()
        for i in players:
            if i.country==nationality:
                lista.append(i)
        return sorted(lista,key=lambda t:t.total,reverse=True)

        


main()
