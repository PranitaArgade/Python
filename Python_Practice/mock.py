name=input("Enter a string:")
vowels="aeiouAEIOU"
count=0
for ch in name:
    if ch in vowels:
        
        count+=1
print(count)
