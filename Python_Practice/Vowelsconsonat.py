# Count vowels and consonants in a string
str_val="Hello World"
vowels="aeiouAEIOU"
v=c=0
for ch in str_val:
    if ch.isalpha():
        if ch in vowels:
            v+=1
        else:
            c+=1
print("vowels:",v)
print("consonant: ",c)


















