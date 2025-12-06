#Create Set

num={1,2,3,4}
print(num)

#Empty set
stud=set()
print(stud)
print(type(stud))

#add elements
stud.add(1)
stud.add(2)
stud.add(5)

print(stud)

stud.remove(5)
print(stud)

print(stud.pop())

Set1={1,3,4,5}
Set2={7,8,4,5}
print(Set1.union(Set2))
print(Set1)
print(Set2)

print(Set1.intersection(Set2))
