# Modern Snake Game

A polished, modern Snake game built with Python and Pygame.

## Features
- Smooth grid-based movement.
- Increasing difficulty (speed increases as you score).
- Score tracking.
- Game Over and Restart functionality.
- Modern color palette.

## Prerequisites
- Python 3.x

## Setup

1. **Navigate to the game directory**:
   ```bash
   cd snake_game
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install pygame
   ```

## How to Play

1. **Run the game**:
   ```bash
   python main.py
   ```

2. **Controls**:
   - **Arrow Keys**: Move the snake.
   - **'R' Key**: Restart the game (from Game Over screen).
   - **Close Window**: Exit the game.

3. **Objective**:
   - Eat the red food to grow and increase your score.
   - Avoid hitting the walls or your own tail.
