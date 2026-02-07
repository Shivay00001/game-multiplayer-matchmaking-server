import time
import random
from src.matchmaker import Matchmaker
from src.player import Player

def main():
    print("--- Multiplayer Matchmaking Server ---")
    
    server = Matchmaker(lobby_size=3) # 3v3 or Battle Royale trio
    
    # Simulate players joining
    player_names = ["Ninja", "Shroud", "DrDisrespect", "TimTheTatman", "Summit1g", 
                    "PewDiePie", "XQC", "Myth", "Pokimane", "Tfue", "S1mple", "Faker"]
    
    print("🚀 Players joining queue...")
    
    for name in player_names:
        elo = random.randint(800, 2200) # Random Skill
        p = Player(name, elo)
        server.enqueue_player(p)
        
        # Simulate tick
        server.process_queues()
        time.sleep(0.2) 

    # Remaining in queue
    print("\n--- Queue Status ---")
    for tier, q in server.queues.items():
        print(f"{tier}: {len(q)} waiting")

if __name__ == "__main__":
    main()
