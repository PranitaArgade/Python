#Create file

with open("Practice.txt",'w') as f:
    f.write("Hii Everyone\nwe are learninhg file I/O \n")
    f.write("Using java.\nand i like programing using java.")

# WAF TO replace all occurrence of  java name with python

with open("Practice.txt",'r') as f:
    data=f.read()
    print(data)
    new_data=data.replace("java", "Python")
    print(new_data)

with open("Practice.txt",'w')as f:
    f.write(new_data)


#search learning word is exits or not in file

word="Everyone"

with open("Practice.txt",'r')as f:
    data=f.read()
    if(data.find(word)!= -1):
        print("found")
    else:
        print("Not found")

#WAF to find which line of file exits word "PYTHON "first occur .return -1 if not occurr

def Check():
    word="Python"
    data=True
    line_no=1
    with open("Practice.txt",'r') as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1

print(Check())
    
#print even nymbers in a file
with open("demo.txt",'w')as f:
    numbers=[2,5,6,7,8]
    for n in numbers:
        f.write(str(n)+", ")

count=0
with open("demo.txt","r")as f:
    data= f.read()
    nums=data.split(",")
    for val in nums:
        val=val.strip()
     
        if(  val and int(val) % 2==0):
            print(val)
            count+=1

print("Total Even numbers: ",count)
        

