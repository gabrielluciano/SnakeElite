import pygame
from enum import Enum
from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, CELL_SIZE, SNAKE_COLOR, SNAKE_GAP, DEFAULT_MOVE_INTERVAL_SECONDS, FAST_MOVE_INTERVAL_SECONDS

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class SnakePart:
    def __init__(self, x, y):
        self.set_coordinates(x, y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y, CELL_SIZE, CELL_SIZE)

class Snake:
    def __init__(self):
        self.offsets = {
            Direction.RIGHT: (SNAKE_GAP + CELL_SIZE, 0),
            Direction.LEFT: (-SNAKE_GAP - CELL_SIZE, 0),
            Direction.UP: (0, -SNAKE_GAP - CELL_SIZE),
            Direction.DOWN: (0, SNAKE_GAP + CELL_SIZE)
        }
        self.move_timer = 0
        self.last_direction = Direction.RIGHT
        self.body = [SnakePart(WINDOW_WIDTH / 2 - CELL_SIZE / 2, WINDOW_HEIGHT / 2 - CELL_SIZE / 2)]

    def grow(self):
        tail = self.body[-1]

        dx, dy = self.offsets[self.last_direction]
        self.body.append(SnakePart(tail.x - dx, tail.y - dy))

    def move(self, dt, fast, direction):
        self.move_timer += dt
                
        if (self.last_direction == Direction.UP and direction == Direction.DOWN) or \
           (self.last_direction == Direction.DOWN and direction == Direction.UP) or \
           (self.last_direction == Direction.LEFT and direction == Direction.RIGHT) or \
           (self.last_direction == Direction.RIGHT and direction == Direction.LEFT):
            # Prevent reversing direction
            direction = self.last_direction
            fast = False

        interval = FAST_MOVE_INTERVAL_SECONDS if fast else DEFAULT_MOVE_INTERVAL_SECONDS
        if self.move_timer < interval:    
            return
        
        self.move_timer = 0
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].set_coordinates(self.body[i-1].x, self.body[i-1].y)
            
        head = self.body[0]
        x, y = self.offsets[direction]

        self.body[0].set_coordinates(head.x + x, head.y + y)
        self.last_direction = direction

    def get_last_direction(self):
        return self.last_direction
        
    def __iter__(self):
        return iter(self.body)

class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Game Loop Example")
        self.clock = pygame.time.Clock()

    def start(self):
        self.running = True
        snake = Snake()
        direction = snake.get_last_direction()
        snake.grow()
        snake.grow()
        dt = 0
        while self.running:
            self.screen.fill((0, 0, 0))

            fast = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        direction = Direction.UP
                    elif event.key == pygame.K_s:
                        direction = Direction.DOWN
                    elif event.key == pygame.K_a:
                        direction = Direction.LEFT
                    elif event.key == pygame.K_d:
                        direction = Direction.RIGHT
            
            keys = pygame.key.get_pressed()

            fast = (keys[pygame.K_w] and direction == Direction.UP) or \
                (keys[pygame.K_s] and direction == Direction.DOWN) or \
                (keys[pygame.K_a] and direction == Direction.LEFT) or \
                (keys[pygame.K_d] and direction == Direction.RIGHT)

            snake.move(dt, fast, direction)

            for snake_part in snake:
                pygame.draw.rect(self.screen, SNAKE_COLOR, snake_part.get_coordinates())

            pygame.display.flip()
            dt = self.clock.tick(FPS) / 1000

        pygame.quit()