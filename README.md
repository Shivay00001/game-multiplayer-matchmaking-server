# Game Multiplayer Matchmaking Server

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Algorithms](https://img.shields.io/badge/Game_Server-Matchmaking-blue.svg)](https://en.wikipedia.org/wiki/Matchmaking_(video_games))
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade matchmaking server** for multiplayer games. This repository uses a skill-based matching algorithm (bucket-based queueing) to group players with similar Elo ratings into fair lobbies.

## 🚀 Features

- **Skill-Based Matchmaking**: Groups players by Elo range (e.g., Bronze, Silver, Gold).
- **Latency Optimization**: Prioritizes players with similar ping (simulated).
- **Lobby Management**: Creates game sessions when a queue fills up.
- **Queue Expansion**: Gradually widens skill search range if wait time is too long.

## 📁 Project Structure

```
game-multiplayer-matchmaking-server/
├── src/
│   ├── matchmaker.py     # Queue Logic
│   ├── player.py         # Player Entity
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/game-multiplayer-matchmaking-server.git

# Run Matchmaker
python src/main.py
```

## 📄 License

MIT License
