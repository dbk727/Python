class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
l1=int(input("enter the length of first rectangle:"))
b1=int(input("enter the breadth of first rectangle:"))
r1=Rectangle(l1,b1)
print('area of first rectangle:',r1.area())
print('perimeter of first rectangle:',r1.perimeter())

l2=int(input("enter the length of second rectangle:"))
b2=int(input("enter the breadth of second rectangle:"))
r2=Rectangle(l2,b2)
print('area of second rectangle:',r2.area())
print('perimeter of second rectangle:',r2.perimeter())

if r1.area()>r2.area()q3 :
    print('first rectangle is largest')
else:
    print('second rectangle is largest')
