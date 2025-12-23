#create a empty dictionaru
student={}
student["name"]="Pranita"
student["age"]=21
print(student)

#update
student["city"]="Sangamner"
print(student)

student["age"]=23
print(student)

student["marks"]=(90,87,70)
print(student)

#using in

if "age" in student:
    print("key found ",student["age"],sep=" ")
else:
    print("not found ")


#del
del student["city"]
print(student)

student.pop("age")
print(student)