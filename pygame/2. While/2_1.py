import pygame

pygame.init()

window_size = (200, 200)
black = (0, 0, 0)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Я слежу за тобой!")

font = pygame.font.SysFont(None, 100)

count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.ACTIVEEVENT:
            if event.state == 2 and event.gain == 0:
                count += 1

    screen.fill(black)

    text = font.render(str(count), True, (255, 0, 0))
    text_rect = text.get_rect(
        center=(window_size[0] // 2, window_size[1] // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()
