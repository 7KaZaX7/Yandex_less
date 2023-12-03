class Point:
    def __init__(self, name, x, y):
        self.name, self.x, self.y, self.tup = name, x, y, (x, y)

    def __str__(self):
        return f'{self.name}{self.tup}'

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.tup