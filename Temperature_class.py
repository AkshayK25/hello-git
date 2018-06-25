class Temprature(object):
  def  convert_fahrenhiet(self,celsius):
    return (celsius*(9/5))+32

  def convert_celsius(self,farenhiet):
    return (farenhiet-32)*(5/9)

t = Temprature()
print(t.convert_fahrenhiet(0),'F')
print(t.convert_celsius(212),'~ Celc')
