class Emp:
    def __init__(self,name,role,dept,sal):
        self.name=name
        self.role=role
        self.dept=dept
        self.sal=sal

    def showdetails(self):
        print(self.name)
        print(self.role)
        print(self.dept)
        print(self.sal)
    


class Engineer(Emp):
    def __init__(self,address,age):
        self.address=address
        self.age=age
        super().__init__("miss pranita","Software developer","IT",200000000)

E1=Engineer("Sangamner",23)
E1.showdetails()