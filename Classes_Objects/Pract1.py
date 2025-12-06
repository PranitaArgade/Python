#create class
class Student:
    
    def __init__(self,name):      #Constructor
        self.name=name
    
    
s1=Student("Pranita")
print(s1.name)

class Vehcile:
    Name="Marcedes"

    def __init__(self,name,color):
        self.Name=name
        self.color=color

    def Speed(self):       #method
        print("Speed 5m/s")
v1=Vehcile("honda","white")
print(v1.Name)
v1.Speed()        