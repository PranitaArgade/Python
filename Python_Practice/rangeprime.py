#print prime numbers from 1 to 100
count=0
for n in range(1,101):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                count+=1
                print(" Not prime number:",n)
                break
        
    else:
        print("number less than 1")
print("Count:",count)
    