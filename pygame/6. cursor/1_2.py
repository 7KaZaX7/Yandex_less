import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Герой двигается!")
FPS = 60
clock = pygame.time.Clock()

person = pygame.image.load(os.path.join("data", "creature.png"))

pygame.mouse.set_visible(False)


speed = 10


class Creature:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10
        self.tic = 60

    def update(self):
        if keys[pygame.K_LEFT]:
            self.x -= speed
        if keys[pygame.K_RIGHT]:
            self.x += speed
        if keys[pygame.K_UP]:
            self.y -= speed
        if keys[pygame.K_DOWN]:
            self.y += speed

    def draw(self):
        screen.blit(person, (self.x, self.y))


main = Creature()
running = True
while running:
    screen.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            main.update()
    main.draw()

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
