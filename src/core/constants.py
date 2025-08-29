from enum import Enum

# General
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

# Game
CELL_SIZE = 20
DEFAULT_MOVE_INTERVAL_SECONDS = 0.25
FAST_MOVE_INTERVAL_SECONDS = 0.08

# Snake
SNAKE_COLOR = (12, 189, 48) 
SNAKE_GAP = 3

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
