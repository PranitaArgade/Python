#fibonnaci series is a sequence where each number is a sum of previous two numbers.it starts  with 0 and 1.
#The underscore _ is used as a dummy variable when the loop variable is not required. It improves code readability.
n=eval(input("Enter number:"))
a,b=0,1
for _ in range(n):
    print(a,end=" ")
    a,b=b,a+b
print()

#Fibonacci series using while loop
num=eval(input("Enter number: "))
a,b=0,1
i=0
while(i<num):
    print(a,end=" ")
    a,b=b,a+b
    i+=1
