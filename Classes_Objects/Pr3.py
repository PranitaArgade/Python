class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,order2):
        return self.price>order2.price
  
e1=Order("chips",20)
e2=Order("Fruits",90)

print(e1>e2)
print(e1<e2)