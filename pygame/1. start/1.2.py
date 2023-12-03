import pygame


def draw_square(screen, widht, height):
    color = pygame.Color('red')
    pygame.draw.rect(screen, color,
                     (1, 1, widht - 2, height - 2), 0)


if __name__ == '__main__':
    pygame.init()
    height, width = input().split()
    size = int(width), int(height)
    screen = pygame.display.set_mode(size)
    draw_square(screen, int(width), int(height))
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()
