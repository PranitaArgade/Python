class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def Area(self):
        area=3.14*self.radius**2
        return area
    
    def Perimeter(self):
        per=2*3.14*self.radius
        return per

C1=Circle(2)
result=C1.Area()
print(result)

per=C1.Perimeter()
print(per)