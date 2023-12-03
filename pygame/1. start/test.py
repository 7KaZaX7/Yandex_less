import pygame
import time

pygame.init()
screen = pygame.display.set_mode((600, 600))  # flags=pygame.NOFRAME
pygame.display.set_caption("My Games")

icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

square = pygame.Surface((300, 300))
square.fill((255, 0, 0))

screen.fill((100, 255, 100))

myFont = pygame.font.SysFont("serif", 50)
textSurface = myFont.render("Hello World!", False, (0, 0, 0))


Ether = pygame.image.load("img/icon.png")

while True:

    screen.blit(square, (150, 150))
    screen.blit(textSurface, (170, 100))
    screen.blit(Ether, (240, 240))

    pygame.draw.circle(square, (0, 0, 0), (150, 150), 160)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255, 100, 100))
                square.fill((0, 255, 0))
            elif event.key == pygame.K_g:
                screen.fill((100, 255, 100))
                square.fill((0, 0, 255))
            elif event.key == pygame.K_b:
                screen.fill((100, 100, 255))
                square.fill((255, 0, 0))
