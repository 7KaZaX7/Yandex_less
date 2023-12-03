import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Перетаскивание")

square_x = 0
square_y = 0
square_size = 100

green = (0, 255, 0)
black = (0, 0, 0)

is_pressed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if square_x <= event.pos[0] <= square_x + square_size and square_y <= event.pos[1] <= square_y + square_size:
                    is_pressed = True

                    i_mouse_x = event.pos[0]
                    i_mouse_y = event.pos[1]
                    i_square_x = square_x
                    i_square_y = square_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_pressed = False

    if is_pressed:
        delta_x = pygame.mouse.get_pos()[0] - i_mouse_x
        delta_y = pygame.mouse.get_pos()[1] - i_mouse_y

        square_x = i_square_x + delta_x
        square_y = i_square_y + delta_y

    screen.fill(black)

    pygame.draw.rect(
        screen, green, (square_x, square_y, square_size, square_size))

    pygame.display.update()
