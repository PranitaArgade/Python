#print the elements

fruits=["banana","mango","chikku","orange"]
for el in fruits:
    print(el)

#search and item

nums=(1,4,8,16,32)
x=int(input("Enter value: "))
for val  in nums:
    if(val==x):
        print("found")
        break


#print number from 1 to 100

for i in range(1,101):
    print(i)

#print 100 to 1

for j in range(100,0,-1):
    print(j)

#print table of n number

n=int(input("Enter a number: "))
sta=1
en=11
for mul in range(sta,en):
    print(n*sta)
    sta+=1

#or

N=int(input("Enter a number: "))
for num in range(1,11):
    print(N*num)
    
#Factorial of first n numbers
value=int(input("Enter value of fact:"))
fact=1
for i in range(1,value+1):
    fact=fact*i

print("Factorial :",fact)