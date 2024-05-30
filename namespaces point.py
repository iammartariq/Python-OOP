class Point:

    x = 0
    y = 0
    count = 0

    def setx(self, xcoord):
        self.x = xcoord

    def sety(self, ycoord):
        self.y = ycoord

    def get(self):
        return self.x, self.y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def assign_ID(self):
        Point.count += 1
        self.ID = Point.count
        return self.ID
    
p1 = Point()
p1.setx(4)
p1.sety(7)
p1.move(2,2)
print(p1.get())
print(p1.assign_ID())
print(p1.assign_ID())