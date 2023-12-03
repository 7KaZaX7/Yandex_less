import pygame


def draw_circle(screen, N, K):
    colors = [(0, 0, 255), (255, 0, 0),  (0, 255, 0)]
    width, height = screen.get_size()
    while K > 0:
        pygame.draw.circle(
            screen, colors[K % 3], (width // 2, height // 2), N * K)
        K -= 1


if __name__ == '__main__':
    pygame.init()
    N, K = input().split()
    size = 2 * int(N) * int(K), 2 * int(N) * int(K)
    screen = pygame.display.set_mode(size)
    draw_circle(screen, int(N), int(K))
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()
