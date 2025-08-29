from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE,SNAKE_GAP, DEFAULT_MOVE_INTERVAL_SECONDS, FAST_MOVE_INTERVAL_SECONDS, Direction

class SnakePart:
    def __init__(self, x, y):
        self.set_coordinates(x, y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y, CELL_SIZE, CELL_SIZE)

class Snake:
    def __init__(self, initial_length=3):
        self.offsets = {
            Direction.RIGHT: (SNAKE_GAP + CELL_SIZE, 0),
            Direction.LEFT: (-SNAKE_GAP - CELL_SIZE, 0),
            Direction.UP: (0, -SNAKE_GAP - CELL_SIZE),
            Direction.DOWN: (0, SNAKE_GAP + CELL_SIZE)
        }
        self.move_timer = 0
        self.last_direction = Direction.RIGHT
        self.body = [SnakePart(WINDOW_WIDTH / 2 - CELL_SIZE / 2, WINDOW_HEIGHT / 2 - CELL_SIZE / 2)]
        [self.grow() for _ in range(initial_length - 1)]

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
