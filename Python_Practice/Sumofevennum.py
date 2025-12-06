#Given a list of integers, find the sum of all even numbers
arr=[22,44,11,21,4,6]
total=0
for num in arr:
    if num%2==0:
        total+=num
print("Sum of all even number:",total)