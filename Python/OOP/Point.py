# math function for sqrt evaluation
import math
# Define the class Point that has:
# Two attributes, x and y - the coordinates of the point on the plane


class Point:
    # A constructor that accepts two arguments, x and y, that initialize the corresponding attributes.
    # These arguments should have default value of 0.0
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    # A method distance_to_origin() that returns the distance from the
    # point to the origin. The formula for that is
    def distance_to_origin(self):
        return math.sqrt(self.x*self.x + self.y * self.y)

    # A method reflect(), that reflects the point with respect to the x- or y-axis:
    # accepts one argument axis,
    # if axis="x" , it sets the y (not a typo!) attribute to the negative value of the y attribute,
    # if axis="y", it sets the x attribute to the negative value of the x attribute,
    # for any other value of axis, prints an error message.
    def reflect(self, origin):
        self.origin = origin

        if origin == "x":
            self.y = self.y * -1
        elif origin == "y":
            self.x = self.x * -1


pt = Point(3.0)
pt.reflect("y")
print(pt.x, pt.y)
pt.y = 4.0
print(pt.distance_to_origin())
