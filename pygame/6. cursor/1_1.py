import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Свой курсор мыши")

cursor_image = pygame.image.load(os.path.join("data", "cursor.png"))
cursor_image = pygame.transform.scale(cursor_image, (50, 50))
cursor_rect = cursor_image.get_rect()
pygame.mouse.set_visible(False)

running = True
while running:
    cursor_rect.center = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    if pygame.mouse.get_focused():
        screen.blit(cursor_image, cursor_rect)

    pygame.display.update()


pygame.quit()
