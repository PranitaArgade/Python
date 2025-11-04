#List is an built in  datype which is used to store different types of elements.
#Create list

Student=["Pranita",22,86.97,"Sangamner"]
print(Student)
print(type(Student))

#Add element at the end of list

Student.append("BEIT")
print(Student)

#Sort list in ascending
marks=[80,50,85]
marks.sort()

print(marks)

#Sort in descendig

marks.sort(reverse=True)
print(marks)

#reverse list
Student.reverse()
print(Student)

marks.reverse()
print(marks)

#Insert elemebts at specific elements
marks.insert(1,70)
print(marks)

marks.insert(2,70)
print(marks)

#Remove list element of first occurence
marks.remove(70)
print(marks)


#Remove elements at index
marks.pop(1)
print(marks)

#length of list
print(len(marks))
