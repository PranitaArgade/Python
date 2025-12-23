#Given a string to find the non repeating charcter.

s=input("Enter a string: ")
freq={}
for ch in s:
        freq[ch]=freq.get(ch,0)+1

for ch in s:
    if freq[ch]==1:
        print(ch)
        
#check num is pallindrome or not

num=int(input("Enter a num:"))
temp=num
rev=0
while(num!=0):
     rem=num%10
     rev=rev*10+rem
     num=num//10

if(rev==temp):
     print("pallindrome")
else:
     print("not pallindrome")

        
   




            



    
