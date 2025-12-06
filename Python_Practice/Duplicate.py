#Given an array, remove duplicate elements
arr=[1,2,3,3,3,4,4,5,6]
unique=list(dict.fromkeys(arr))
print(unique)