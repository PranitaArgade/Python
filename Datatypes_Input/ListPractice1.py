#WAP to ask user to enter there  3 fav movies name and store in a list.
mov1=input("Enter first movie: ")
mov2=input("Enter  Second movie: ")
mov3=input("Enter Third movie: ")
movie=[mov1,mov2,mov3] #we can used append method also
print(movie)

#WAP To check if a list contain pallindrom of number.(use copy method)
list1=[1,2,3,6,1]
list1_copy=list1.copy()
list1_copy.reverse()

if(list1_copy==list1):
    print("Pallindrome ")
else:
    print("Not pallindrome")

#Store value in list and sort

alpha=['d','a','f','y','o']
alpha.sort()
print(alpha)