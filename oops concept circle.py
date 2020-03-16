from math import pi
class shape:
    def __init__(self,color = None):
        self.color = color
    def get_color(self):
        return self.color
    def __str__(self):
        return 'the color is '+ self.color
class Circle(shape):
    def __init__(self, color , radius):
        #super().__init__(color)
        self.color = color
        self.radius = radius
    def get_area(self):
        return pi*self.radius**2
    def get_circumference(self):
        return 2*pi*self.radius
s = shape('red')
print(s.__str__())
r = Circle('blue', 2)
print(r.get_color())
print(r.get_area())
print(r.__str__())