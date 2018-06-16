class Base1(object):
    def __init__(self):
        self.str1 = "Akshay"
        print("Base1 called")


class Base2(object):
    def __init__(self):
        self.str2 = "Kumar"
        print("Base2 called")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("We are In Derived ClaSS")

    def print_strs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.print_strs()

"""
output: 
   Base1 called
   Base2 called
   We are In Derived ClaSS
   Akshay Kumar
"""