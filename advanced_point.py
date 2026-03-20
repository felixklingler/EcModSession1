# need to import from color_point
from color_point import ColorPoint

class AdvancedPoint(ColorPoint):
    # class variables
    COLORS = ["red", "green", "blue", "yellow", "black", "white"]# validates if a chosen color is in the official list
    def __init__(self, x, y, color):
        # check the color
        if color not in self.COLORS:
            raise ValueError(f"invalid color: need to be one of {self.COLORS}")
        # call the init from ColorPoint
        self._x = x # you can get the value, but not set it anymore
        self._y = y
        self._color = color

    @ property # @ is a decorator
    def x(self):
        return self._x

    @ property
    def y(self):
        return self._y

    @ property
    def color(self):
        return self._color

    @ classmethod
    def add_color(cls, color):
        # add a new color to the list
        cls.COLORS.append(color)

    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    @staticmethod
    def from_dict(d): # "factory" allows to create from a dictionary
        x = d["x"]
        y = d["y"]
        color = d["color"]
        return AdvancedPoint(x, y, color)


p0 = AdvancedPoint.from_dict({"x":1, "y":2, "color":"red"})
p1 =  AdvancedPoint(1, 2, "red")
print(p1)
p2 = AdvancedPoint(3, 4, "white")
print(p2)
print(p1.x) #property 'x' of 'AdvancedPoint' object has no setter
AdvancedPoint.add_color("coral")
p3 = AdvancedPoint(1, 2, "coral")
print(p3)
print(AdvancedPoint.distance_2_points(p1, p3))