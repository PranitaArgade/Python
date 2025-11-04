#Calculator
def add(a,b):
    addition=a+b
    return addition
def sub(a,b):
    substract=a-b
    return substract

def mul(a,b):
    multi=a*b
    return multi

def div(a,b):
    division=a/b
    return division

while(True):
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Close")
    a=int(input("Enter value of a="))
    b=int(input("Enter valie of b="))
    ch=int(input("Enter choice="))
    if(1==ch):
        adds=add(a,b)
        print(adds)
    elif(2==ch):
        subtract=sub(a,b)
        print(subtract) 
    elif(3==ch):
        multipli=mul(a,b)
        print(multipli)
    elif(4==ch):
        division=div(a,b)
        print(division)
    elif(5==ch):
        break
           









