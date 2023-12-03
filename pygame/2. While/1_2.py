import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
window_width = 800
window_height = 600
black = (0, 0, 0)
white = (255, 255, 255)

window = pygame.display.set_mode((window_width, window_height))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.speed = 100
        self.direction = [1, -1]

    def update(self, dt):
        self.x += self.speed * self.direction[0] * dt
        self.y += self.speed * self.direction[1] * dt

        if self.x - self.radius <= 0 or self.x + self.radius >= window_width:
            self.direction[0] *= -1

        if self.y - self.radius <= 0 or self.y + self.radius >= window_height:
            self.direction[1] *= -1

    def draw(self):
        pygame.draw.circle(
            window, white, (int(self.x), int(self.y)), self.radius)


balls = []

while True:
    window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            balls.append(Ball(x, y))

    dt = clock.tick(60) / 1000.0

    for ball in balls:
        ball.update(dt)
        ball.draw()

    pygame.display.update()
