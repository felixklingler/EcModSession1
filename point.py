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




p1= Point(1,2)
p2= Point(3,4)
p3= Point("Bob",[1,2,3])


print(p1.x, p1.y)
print(p2.x, p2.y)
print(p3.x, p3.y) # not ideal
print(p1)