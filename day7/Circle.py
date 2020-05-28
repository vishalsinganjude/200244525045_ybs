'''
2. Write a Python class named Circle constructed by a radius and two
    methods which will compute the area and the perimeter of a circle.
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        return pi*self.radius**2

    def perimeter(self):
        pi = 3.14
        return 2*pi*self.radius
circle = Circle(5)
area = circle.area()
perimeter = circle.perimeter()
print("Area Of Circle : ", format(area,'.2f'))
print("Area Of Perimeter : ", format(perimeter,'.2f'))
