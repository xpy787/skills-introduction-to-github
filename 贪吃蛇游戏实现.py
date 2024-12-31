import random
import pygame

class Snake:
    def __init__(self):
        self.positions = [(100, 100), (90, 100), (80, 100)]
        self.direction = "RIGHT"
        self.length = 3

    def move(self):
        current = self.positions[0]
        if self.direction == "RIGHT":
            new_head = (current[0] + 10, current[1])
        elif self.direction == "LEFT":
            new_head = (current[0] - 10, current[1])
        elif self.direction == "UP":
            new_head = (current[0], current[1] - 10)
        elif self.direction == "DOWN":
            new_head = (current[0], current[1] + 10)

        # 检查是否碰到边界并处理
        if new_head[0] < 0:
            new_head = (790, new_head[1])
        elif new_head[0] >= 800:
            new_head = (0, new_head[1])
        elif new_head[1] < 0:
            new_head = (new_head[0], 590)
        elif new_head[1] >= 600:
            new_head = (new_head[0], 0)

        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
snake = Snake()
food = (random.randrange(0, 790, 10), random.randrange(0, 590, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"

    snake.move()
    # 吃到食物
    if snake.positions[0] == food:
        snake.length += 1
        food = (random.randrange(0, 790, 10), random.randrange(0, 590, 10))

    # 绘制
    screen.fill((0, 0, 0))
    for pos in snake.positions:
        pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 10, 10))
    pygame.display.flip()
    clock.tick(15)



