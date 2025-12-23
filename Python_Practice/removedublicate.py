#Remove duplicates from a list using set
list=[1,2,2,3,3,4,4]
unique=[]
for num in list:
    if num not in unique:
        unique.append(num)

print(unique)
    