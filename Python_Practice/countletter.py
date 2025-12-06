#. Given a string, count frequency of each character

str_val="cognizant"
freq={}

for ch in str_val:
    freq[ch]=freq.get(ch,0)+1
print(freq)


#for loop

str1="hello"
fre={}
for ch in str1:
    if ch in fre:
        fre[ch]+=1
    else:
        fre[ch]=1
print(fre)
