import time
from collections import deque
from src.player import Player

class Matchmaker:
    def __init__(self, lobby_size=4):
        self.lobby_size = lobby_size
        # Buckets for different ranks
        self.queues = {
            "Bronze": deque(),   # 0-1000
            "Silver": deque(),   # 1000-1500
            "Gold": deque(),     # 1500-2000
            "Diamond": deque()   # 2000+
        }
        self.active_lobbies = []

    def get_tier(self, elo):
        if elo < 1000: return "Bronze"
        elif elo < 1500: return "Silver"
        elif elo < 2000: return "Gold"
        return "Diamond"

    def enqueue_player(self, player: Player):
        tier = self.get_tier(player.elo)
        self.queues[tier].append(player)
        print(f"📥 {player} joined {tier} Queue.")

    def process_queues(self):
        """Attempts to form lobbies."""
        for tier, queue in self.queues.items():
            if len(queue) >= self.lobby_size:
                lobby = []
                # Pop N players
                for _ in range(self.lobby_size):
                    lobby.append(queue.popleft())
                
                self._create_match(tier, lobby)

    def _create_match(self, tier, players):
        match_id = f"MATCH-{int(time.time())}-{tier}"
        avg_elo = sum(p.elo for p in players) / len(players)
        print(f"✅ Created {tier} Match {match_id} (Avg Elo: {avg_elo:.0f})")
        print(f"   Players: {', '.join([p.id for p in players])}")
        self.active_lobbies.append(match_id)

    def expand_search(self):
        """Mock: If players wait too long, move them to adjacent queues (implied)."""
        pass
