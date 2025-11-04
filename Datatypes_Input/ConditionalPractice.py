#WAP to check number is even or odd

number=int(input("Enter number: "))
if(number%2==0):
    print("Even number")
else:
    print("odd number")

#WAP To find the greatest of three number entered  by user
 
num1=int(input("Enter number first: "))
num2=int(input("Enter number second: "))
num3=int(input("Enter number three: "))

if(num1>num2 and num1>num3):
    print(num1 ," is graeter ")
elif(num2>num1 and num2>num3):
    print(num2 ," is geater")
else:
    print(num3 ,"Is greater")

#WAP To check number is multiple of 7 or not

Num=int(input("Enter number:"))
if(Num%7==0):
    print("Number is multiple of 7")
else:
    print("Number is not nmultiple of 7")

print(Num%7==0)