class Circle(object):
     pi = 3.14159

     def __init__(self, radius):
         self.radius = radius

     def area(self):
         return Circle.pi * self.radius * self.radius
