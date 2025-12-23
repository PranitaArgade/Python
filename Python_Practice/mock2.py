#remove dublicates in a list
list_value=[2,2,6,6,7,8]
unique=[]                      #this method preserved order
for n in list_value:
    if n not in unique:
        unique.append(n)

print(unique)

#using set method....it does not preserve order
list3=[2,3,3,4,4,5] 
unique_list=list(set(list3))
print(unique_list)

#using dictionary....preserved oreder

lst=[9,7,0,5,7,9,8]
remove_dublicate=list(dict.fromkeys(lst))
print(remove_dublicate)




#check number is exit or not
list2=[2,4,5,5,6]
n=4
if n in list2:
    print("yes")
else:
    print("no")
