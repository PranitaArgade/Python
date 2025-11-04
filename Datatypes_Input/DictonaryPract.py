#Create Dictionary

Student={
    "name":"Pranita Argade",
    "age":22,
    "Course":"IT"

}
print(type(Student))

print(Student)

#Add elements

Student["job"]="Software Engineer"

#modify value
Student["name"]="Pranita Navnath Argade"
print(Student)

#Access value
print(Student["name"])

#Methods

#key
print(Student.keys())  #tuple format

#Type casting

print(list(Student.keys()))

#values

print(Student.values())

#items -returns all key value pairs

print(Student.items())

print(list(Student.items()))

pair=list(Student.items())

print(pair[0])

#get-returns value according to key ans it returns none if key is not exits

print(Student.get("name"))
print(Student.get("address"))  #none

#update

Student.update({"location":"Pune"})

print(Student)

Student.pop("location")

#clear
Student.clear()
print(Student)