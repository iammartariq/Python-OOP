class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def setRadius(self, r):
        self.radius = r

    def setColor(self, c):
        self.color = c

    def getRadius(self):
        return self.radius
    
    def getColor(self):
        return self.color
    
    def getCircumference(self):
        return 2*3.142*self.getRadius()
    
    def getArea(self):
        return 3.142*(self.getRadius()**2)
    

c1 = Circle(4, "blue")
print(c1.getArea())
print(c1.getCircumference())
