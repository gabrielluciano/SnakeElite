import pygame
from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, SNAKE_GAP, DEFAULT_MOVE_INTERVAL_SECONDS, FAST_MOVE_INTERVAL_SECONDS, SNAKE_COLOR, Direction

class SnakePart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(SNAKE_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))

    def set_position(self, x, y):
        self.rect.topleft = (x, y)

class Snake:
    def __init__(self, sprite_group, initial_length=3):
        self.offsets = {
            Direction.RIGHT: (SNAKE_GAP + CELL_SIZE, 0),
            Direction.LEFT: (-SNAKE_GAP - CELL_SIZE, 0),
            Direction.UP: (0, -SNAKE_GAP - CELL_SIZE),
            Direction.DOWN: (0, SNAKE_GAP + CELL_SIZE)
        }
        self.move_timer = 0
        self.last_direction = Direction.RIGHT
        self.body = []

        head_x = WINDOW_WIDTH / 2 - CELL_SIZE / 2
        head_y = WINDOW_HEIGHT / 2 - CELL_SIZE / 2
        head = SnakePart(head_x, head_y)
        self.body.append(head)
        sprite_group.add(head)

        [self.grow(sprite_group) for _ in range(initial_length - 1)]

    def grow(self, sprite_group):
        tail = self.body[-1]

        dx, dy = self.offsets[self.last_direction]
        part = SnakePart(tail.rect.x - dx, tail.rect.y - dy)
        sprite_group.add(part)
        self.body.append(part)

    def move(self, dt, fast, direction):
        self.move_timer += dt
                
        if self._is_reverse(direction):
            # Prevent reversing direction
            direction = self.last_direction
            fast = False

        interval = FAST_MOVE_INTERVAL_SECONDS if fast else DEFAULT_MOVE_INTERVAL_SECONDS
        if self.move_timer < interval:    
            return
        
        self.move_timer = 0
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].set_position(self.body[i-1].rect.x, self.body[i-1].rect.y)
            
        head = self.body[0]
        x, y = self.offsets[direction]

        self.body[0].set_position(head.rect.x + x, head.rect.y + y)
        self.last_direction = direction

    def _is_reverse(self, direction):
        return (self.last_direction == Direction.UP and direction == Direction.DOWN) or \
               (self.last_direction == Direction.DOWN and direction == Direction.UP) or \
               (self.last_direction == Direction.LEFT and direction == Direction.RIGHT) or \
               (self.last_direction == Direction.RIGHT and direction == Direction.LEFT)

    def get_last_direction(self):
        return self.last_direction
        
    def check_self_collision(self):
        head = self.body[0]
        hits = pygame.sprite.spritecollide(head, self.body, False)
        return len(hits) > 1

    def __iter__(self):
        return iter(self.body)
