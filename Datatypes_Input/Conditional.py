#Program 1: To check traffic light signal.

light=input("Light color: ")
if(light=="red"):
    print("Stop")
elif(light=="Green"):
    print("Go")
elif(light=="yellow"):

    print("Look")
else:
    print("Light broken")

#Program 2: To check grade

marks=float(input("Marks : "))
if(marks>=90):
    print("A GRADE")
elif(marks>=80 and marks<90):
    print("B Grade")
elif(marks>60 and marks<80):
    print("C grade")
elif(marks>50 and marks>=35):
    print("D grade")
else:
    print("Fail")

