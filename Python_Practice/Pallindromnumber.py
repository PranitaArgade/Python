#check number is pallindrome or not
n=int(input("Enter a number:"))
temp=n
rev=0

while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print("pallindrome number")
else:
    print("not pallindrome")

#check a string is pallindrome or not without slicing
str=input("Enter a string:")
rev=""
for ch in str:
    rev=ch+rev

if(str==rev):
    print("pallindrome")
else:
    print("not pallindrome")

#check a string is pallindrome or not using slicing

strname=input("Enter a string:")
rev=strname[::-1]
if strname==rev:
    print("Pallindrome")
else:
    print("not pallindrome")