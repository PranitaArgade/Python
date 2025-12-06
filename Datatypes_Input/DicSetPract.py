#dictionary
Collection={
    "table":["A piece of furniture","A lists of fact and piece"],
    "cat":["A small animal"]
}
print(Collection)
#how many classroom required in one subject
Subject={"Python","java","Javascript","java","java","Python","C++","C++","C"}
print(Subject)

print(len(Subject),"resquired classes")

#WAP to take 3 subjects from user and stored it into in a dictionary first create empty dictionary and store it one by one . used subjects as key and marks ans value

Subject={}
sub1=input("Enter sub1: ")
marks1=input("Enter marks : ")
Subject[sub1]=marks1


sub2=input("Enter sub1: ")
marks2=input("Enter marks : ")
Subject[sub2]=marks2
sub3=input("Enter sub1: ")
marks3=input("Enter marks : ")
Subject[sub3]=marks3

print(Subject)

#values in set 0 and 9.0

values={
    ("float",9.0),
    ("int",9)
}

print(values)