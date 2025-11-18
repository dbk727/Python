class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2* (self.lr2.length+self.breadth)

r1=Rectangle(10,5)
r2=Rectangle(8,7)
print("Area of r1:",r1.area())
print("Area pf r2:",r2.area())
if r1.area()>r2.area():
    print("Rectangle r1 is bigger")
else: print("Rectangle r2 is bigger")

