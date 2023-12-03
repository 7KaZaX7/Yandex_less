import pygame


def draw_squares(screen, W, N):
    size = W / N
    for i in range(N):
        for j in range(N):
            if i % 2 == 0:
                if j % 2 == 0:
                    pygame.draw.rect(screen, 'black',
                                     (j * size, i * size, size, size))
            else:
                if j % 2 == 1:
                    pygame.draw.rect(screen, 'black',
                                     (j * size, i * size, size, size))


if __name__ == '__main__':
    pygame.init()
    W, N = input().split()
    size = int(W), int(W)
    screen = pygame.display.set_mode(size)
    screen.fill('white')
    draw_squares(screen, int(W), int(N))
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()
