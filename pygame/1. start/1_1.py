import pygame


def draw_diagonals(screen, width, height):
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen.fill(black)
    pygame.draw.line(screen, white, (10, 10), (width - 10, height - 10), 5)
    pygame.draw.line(screen, white, (10, height - 10), (width - 10, 10), 5)


if __name__ == '__main__':
    pygame.init()
    height, width = input().split(' ')
    size = int(width), int(height)
    screen = pygame.display.set_mode(size)
    draw_diagonals(screen, int(400), int(400))
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()
