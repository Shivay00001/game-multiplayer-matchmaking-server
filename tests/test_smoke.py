"""Minimal smoke test for game-multiplayer-matchmaking-server (stdlib-only)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.matchmaker import Matchmaker
from src.player import Player


def test_tier_boundaries():
    mm = Matchmaker()
    assert mm.get_tier(500) == "Bronze"
    assert mm.get_tier(1200) == "Silver"
    assert mm.get_tier(1800) == "Gold"
    assert mm.get_tier(2500) == "Diamond"


def test_lobby_formation():
    mm = Matchmaker(lobby_size=4)
    for i in range(4):
        mm.enqueue_player(Player(f"p{i}", 1200))  # all Silver
    assert len(mm.active_lobbies) == 0
    mm.process_queues()
    assert len(mm.active_lobbies) == 1
    assert len(mm.queues["Silver"]) == 0


def test_partial_queue_no_lobby():
    mm = Matchmaker(lobby_size=4)
    for i in range(3):
        mm.enqueue_player(Player(f"q{i}", 800))  # Bronze
    mm.process_queues()
    assert len(mm.active_lobbies) == 0
    assert len(mm.queues["Bronze"]) == 3
