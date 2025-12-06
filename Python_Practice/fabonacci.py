#Fibonacci Series in Python
num=int(input("Enter number: "))
a,b=0,1
print(a,b,end=" ")
for _ in range(num-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

