import pygame

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.x_0 = 10
        self.y_0 = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, x_0, y_0, cell_size):
        self.x_0 = x_0
        self.y_0 = y_0
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.x_0, y * self.cell_size + self.y_0, self.cell_size, self.cell_size), 1)

    # cell - кортеж (x, y)
    def on_click(self, cell):
        return cell

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.x_0) // self.cell_size
        cell_y = (mouse_pos[1] - self.y_0) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            return self.on_click(cell)

    def color_cell(self, cell, color):
        x, y = cell
        pygame.draw.rect(screen, color, (x * self.cell_size + self.x_0,
                         y * self.cell_size + self.y_0, self.cell_size, self.cell_size))
        pygame.display.flip()

    def invert_color(self, cell):
        for x in range(board.width):
            if cell != (x, cell[1]):
                if (x, cell[1]) not in color_matrix.keys():
                    color_matrix[x, cell[1]] = 'white'
                elif color_matrix[x, cell[1]] == 'white':
                    color_matrix[x, cell[1]] = 'black'
                elif color_matrix[x, cell[1]] == 'black':
                    color_matrix[x, cell[1]] = 'white'
                board.color_cell(
                    (x, cell[1]), color_matrix[x, cell[1]])
            for y in range(board.height):
                if (cell[0], y) not in color_matrix.keys():
                    color_matrix[cell[0], y] = 'white'
                elif color_matrix[cell[0], y] == 'white':
                    color_matrix[cell[0], y] = 'black'
                elif color_matrix[cell[0], y] == 'black':
                    color_matrix[cell[0], y] = 'white'
                board.color_cell(
                    (cell[0], y), color_matrix[cell[0], y])


color_matrix = {}
# поле 5 на 7
board = Board(3, 3)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            cell = board.get_click(event.pos)
            if cell:
                board.invert_color(cell)

    board.render()
    pygame.display.flip()
