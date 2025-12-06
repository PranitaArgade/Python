#Find the second largest element in an array
arr=[1,2,4,8]
first=second=float("-inf")
for num in arr:
    if num>first:
        second=first
        first=num
    elif num>second and num!=first:
        second=num
print("Second largest:",second)
print("largest number:",first)
