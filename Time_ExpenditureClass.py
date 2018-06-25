class Expendituretime(object):

  def __init__(self, hours, mint):
    self.hours = hours
    self.mint = mint

  def addtime(self, t2):
    t3 = Expendituretime(0,0)
    if self.mint+t2.mint > 60:
      t3.hours = (self.mint+t2.mint)//60
    t3.hours = t3.hours+self.hours+t2.hours
    t3.mint = ((self.mint+t2.mint)-60)
    return t3

  def displaytime(self):
    print ("Time is :: %0.2f" % self.hours,"hours and",self.mint,"minutes.")

  def display_minute(self):
    print('Total time in minutes will be - >',(self.hours*60)+ self.mint,"minutes")

a = Expendituretime(2,50)
b = Expendituretime(1,20)
c = Expendituretime.addtime(a,b)
print('---------------------------Welcome to Expenditure class showing time conversion--------------------------------')
c.displaytime()
c.display_minute()
print('-----------------------------End of Program--------------------------------------------------------------------')
