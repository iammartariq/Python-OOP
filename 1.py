# Question:
# Implement a class Shape having one attribute no_of_sides, which is set to 1 by default in the
# constructor.
# From Shape derive a class Rectangle, having attributes length and width, supporting the
# following methods:
#  perimeter( ): returns the perimeter of the rectangle
#  area( ): returns the area of the rectangle
#  Also define appropriate constructor setting both length and width to 0 by default and fixing
# no_of_sides to 4.
# The object when printed should display the following:
# Sides: <number of sides>
# Length: <length>
# Width: <width>
# Perimeter: <perimeter of the rectangle>
# Area: <area of the rectangle>

class Shape:
    def __init__(self, ns = 1):
        self.no_of_sides = ns

class Rectangle(Shape):
    def __init__(self, l = 0, w = 0):
        self.length = l
        self.width = w
        super().__init__(4)

    def perimeter(self):
        return 2*(self.width + self.length)
    
    def area(self):
        return self.width * self.length
    
    def __str__(self):
        s = f"Number of sides: {self.no_of_sides} \n"
        s += f"Length: {self.length} \n"
        s += f"Width: {self.width} \n"
        s += f"Perimeter of the rectangle: {self.perimeter()} \n"
        s += f"Area of the rectangle: {self.area()}"
        return s

r = Rectangle(2, 3)
print(r)

s = Shape(4)
print(s)
