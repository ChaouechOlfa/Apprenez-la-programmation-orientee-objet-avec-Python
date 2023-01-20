class Rectangle:
   def __init__(self, height, width, color="red") :
      self.height=height
      self.width=width
      self.color=color
   def Calculate_area(self):
      return self.width*self.height

rectangle=Rectangle(5,3)
res=rectangle.Calculate_area()
print(res)

   