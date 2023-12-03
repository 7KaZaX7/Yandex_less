class Point:
    def __init__(self, name, x, y):
        self.name, self.x, self.y, self.tup = name, x, y, (x, y)

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __str__(self):
        return f'{self.name}{self.tup}'

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __eq__(self, other):
        return (self.name, self.x, self.y) == (other.name, other.x, other.y)

    def __gt__(self, other):
        return (self.name, self.x, self.y) > (other.name, other.x, other.y)

    def __ge__(self, other):
        return (self.name, self.x, self.y) >= (other.name, other.x, other.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class ColoredPoint(Point):
    def __init__(self, name, x, y, rgb=(0, 0, 0)):
        super().__init__(name, x, y)
        self.rgb = rgb

    def __invert__(self):
        rgb_inv = tuple([255 - i for i in self.rgb])
        return ColoredPoint(self.name, self.y, self.x, rgb_inv)

    def get_color(self):
        return self.rgb

    def get_coords(self):
        return self.tup