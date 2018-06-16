class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (3.14*self.radius**2)
R =int(input("Enter Radius of Circle: "))
obj=circle(R)
print("Area of Circle:",obj.area())