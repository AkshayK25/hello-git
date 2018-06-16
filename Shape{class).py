class Shape:
    def name(self):
        print("Shape mentioned above <>")

class parallelopied(Shape): # single inheritance
    def name(self):
        print("parallelopied")
        # Call name method from parent class.
        super().name()

# Create parallelopied class and call name.
c = parallelopied()
c.name()