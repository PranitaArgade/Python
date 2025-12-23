#Find Missing Number (1 to n)
arr=[1,4,2,5]
n=max(arr)

total=n*(n+1)//2
print("total :",total)
print(total-sum(arr))


#Find Missing Number (1 to n)

add=0
for i in arr:
    add+=i

print("addition: ",add)
print("Missing no: ",total-add)
