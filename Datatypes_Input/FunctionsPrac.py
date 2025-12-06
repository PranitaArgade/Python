#create function 
#def is used to define functions

def sum(a,b):
    return a+b

Sum=sum(10,20)
print(Sum)

#Avearge of 3 numbers

def Average(a,b,c):
    avg=(a+b+c)/3
    return avg

Avgoutput=Average(10,10,10)
print(Avgoutput)

#WAF to print the length of list and list is parameter

def list_len(a):
    return len(a)

result=list_len([1,2,3,4])
print("Length of list",result)

#WAF to print the elements of list in single line .

cities=["Pune","Nashik","Sangamner","Sinner"]

def elements(list):
    for item in list:
        print(item,end=" ")

elements(cities)

#WAF to find the factorial of n number n is a parameter


def facts(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


Factorial=facts(5)
print()
print("Factorial:" ,Factorial)

#Convert USD value into inr
def convert(usd):
    inr=usd*83
    print(usd,"usd= ",inr," inr")

convert(1)

#return odd and even

num=int(input("Enter a number to check odd or even: "))
def Check(num):
    if(num%2==0):
        print("Even number")
    else:
        print("ODD number")

Check(num)
