import time

class Player:
    def __init__(self, player_id, elo, region="US-East"):
        self.id = player_id
        self.elo = elo
        self.region = region
        self.join_time = time.time()

    def __repr__(self):
        return f"[Player {self.id} | Elo: {self.elo}]"
