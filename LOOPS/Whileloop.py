#print number 1 to 10

i=1
while (i<=10):
    print(i)
    i+=1
print("Loop ended")

#print numbers from 100 to 1

num=100
while(num>=1):
    print(num)
    num=num-1

#print multiplication table of n number
num=int(input("Enter a number"))
i=1
while(i<=10):
    mul=num*i
    print(mul)
    i+=1

#print table from 2 to 20


j=2
while(j<=20):
    num=j
    k=1
    while(k<=10):
        mult=num*k
        print(mult,end='\t')
        k+=1
    print()
    j+=1



#table in column wise

k=1
while k<=10:
    j=2
    while(j<=20):
        print(j*k,end='\t')
        j+=1
    print()
    k=k+1

#print the square of element

num=1
while(num<=10):
    print(num**2,'  ')
    num+=1


#print the list of elements

nums=[1,4,9,16,25,36,49,64,81,100]

idx=0
while(idx<len(nums)):
    print(nums[idx])
    idx+=1

#Search for item x in a tuple 

tup=(1,4,9,10,6,7)
x=int(input("Enter value: "))
i=0
while i<len(tup):
    if(tup[i]==x):
        print("found index at ",i)
    i+=1

#WAP to find the sum of first N numbers
n=int(input("Enter value of n: "))
sum=0
i=0
while(i<=n):
    sum=sum+i
    i+=1

print("Sum: ",sum)
    




