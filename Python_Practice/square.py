def mul(a,b):
    if(b==1):
        return a
    else:
        return a*mul(a,b-1)
    


a=int(input())
b=int(input())
result=mul(a,b)
print(result)