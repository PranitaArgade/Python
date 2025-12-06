#Guess the number

import random
a=int(input("Enter range: "))
b=int(input("Enter range of b: "))
target=random.randint(a,b)

while True:
    uservalue=int(input("Enter your target value  or quit: "))
    if(uservalue=="quit"):
        break
    uservalue=int(uservalue)
    if(uservalue==target):
        print("Success..Correct guess")
        break
    elif(uservalue<target):
        print("USERVALUE IS SAMLLER THAN TARGET...")
    else:
        print("User value is greater than target....")

print("Game over!!!!")




    

