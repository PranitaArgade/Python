

def fact(a):
    if(a==0 or a==1):
        return 1
    elif(a<0):
        return -1
    else:
        return a*fact(a-1)
    

factorial=fact(int(input()))
print(factorial)
    

