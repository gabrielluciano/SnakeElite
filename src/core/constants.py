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
INITIAL_SNAKE_LENGTH = 3

# Monster
MONSTER_SPEED = 150  # pixels per second
MONSTER_ASSETS = [
    "assets/monster_1.png",
    "assets/monster_2.png",
    "assets/monster_3.png",
    "assets/monster_4.png"
]

# Leveling
MAX_LEVEL = 4
LEVEL_THRESHOLDS = [0, 50, 100, 150]  # Score needed to reach level 1, 2, 3, 4

# Score
SCORE_FONT_SIZE = 36
SCORE_COLOR = (0, 0, 0)
SCORE_POSITION = (10, 10)
SCORE_INCREMENT = 10

# Fonts
PRIMARY_FONT_PATH = "assets/Jersey15-Regular.ttf"

# Title
GAME_TITLE_FONT_SIZE = 120
GAME_TITLE_COLOR = (12, 189, 48) # Green

# Creator Legend
CREATOR_TEXT = "Created by Gabriel Luciano"
CREATOR_FONT_SIZE = 24
CREATOR_FONT_COLOR = (200, 200, 200) # Light Grey

# Menu
MENU_FONT_SIZE = 80
MENU_SELECTED_COLOR = (255, 255, 0)  # Yellow
MENU_FONT_COLOR = (204, 204, 0) # Darker Yellow

# Game Over
GAME_OVER_FONT_SIZE = 74
GAME_OVER_COLOR = (255, 0, 0)

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
