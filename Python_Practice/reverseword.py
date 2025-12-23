#reverse a words in a string
s="I like coding"
words=s.split()
result=[]
for i in range(len(words)-1,-1,-1):
    result.append(words[i])

print(" ".join(result))


#with slicing


reverse_word=[]
reverse_word=words[::-1]
print(" ".join(reverse_word))

#built in function

final_result=reversed(s.split())
print(" ".join(final_result))