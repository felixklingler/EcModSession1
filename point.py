# what makes a point a point?
# class is like def but for object

class Point: # classes start with capital letters always
    """
    Simple class to represent a point in 2D space.
    """
    def __init__(self, x, y): # if a def is inside a class, it's a method
        #
        # self is the unique structure you will have every time you instantiate a new object
        """
        Constructor for Point Class.
        :param x: x coordinate of the point.
        :param y: y coordniate of the point.
        """
        self.x = x # current x is 12 (example), x is a class attribute
        self.y = y # current y is 14 (example), y is a class attribute
    def __str__(self): # str for string - what is the value i want to see when i print?
        """
        String representation of the point class.
        :return: String representation of the point class.
        """
        return f"P<{self.x},{self.y}>" # returns P<x,y>
    def __repr__(self):
        """
        If the instance is inside of a list, it will be printed nicely
        :return:
        """
        return self.__str__()
    def distance_origin(self):
        """
        Calculates the distance from the origin to the point.
        :return: float, deistance between origin and point.
        """
        return (self.x**2 + self.y**2)**0.5
    def distance_to(self, point):
        """
        Calculates the distance between current point and another point.
        :param point: the other point to calculate the distance to.
        :return: float, distance between current point and another point.
        """
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
    def __lt__(self, other):
        """
        Returns true if self is less than other
        :param other: the other point to compare to.
        :return: True or False
        """
        return self.distance_origin() < other.distance_origin()


p1= Point(1,2)
p2= Point(3,4)
p3= Point("Bob",[1,2,3])


print(p1.x, p1.y)
print(p2.x, p2.y)
print(p3.x, p3.y) # not ideal
print(p1)

print(f"{p2} distance to origin is {p2.distance_origin()}")
# print(f"{p3} distance to origin is {p3.distance_origin()}") # makes error, since values are not float

print(f"the distance between {p1} and {p2} is {p1.distance_to(p2)}")

p1 = Point(6,10)
p2 = Point(6,15)
p3 = Point(12,5)
p4 = Point(1,1)

points = [p1, p2, p3, p4, Point(15,6)] # adding a point without adding a line
print(points)
points.sort() # sorts by "size", which in this case is distance to origin
print(points)