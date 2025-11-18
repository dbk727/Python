class Time:
   def __init__(self,hour,minute,second):
      self.hour=hour
      self.minute=minute
      self.second=second
   def __add__(self,other):
      s=self.second+other.second
      m=self.minute+other.minute
      h=self.hour+other.hour

      if s>=60:
         m+=s //60
         s=s%60

      if m>=60:
         h+= m // 60
         m=m%60

      h=h%24
      return Time(h,m,s)
   def show(self):
      print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

print("enter first time:")
h1=int(input("hour:"))
m1=int(input("minute:"))
s1=int(input("second:"))

print("enter second time:")
h2=int(input("hour:"))
m2=int(input("minute:"))
s2=int(input("second:"))

t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
t3=t1+t2

print("first time:",end="")
t1.show()
print("second time:",end="")
t2.show()
print("sum of time:",end="")
t3.show()
