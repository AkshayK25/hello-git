class Student(object):
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll

  def display(self):
    print('-----------------------Welcome to Database--------------------------------------')
    print('Name::',self.name)
    print('Roll_no.',self.roll)
    return '----------------------My Report details displayed below------------------------'

  def setage(self,age=22):
    self.age=age
    return self.age

  def setmarks(self,marks=88):
    self.marks = marks
    return self.marks

s = Student('Akshay kumar',38)
print(s.display())
print(s.setage(),'years')
print('Acadview marking',s.setmarks())