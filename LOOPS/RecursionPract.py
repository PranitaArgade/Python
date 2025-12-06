#WAF to calculte the sum of n natural number

def Sum(n):
    if(n==0):
        return 0
    else:
        return Sum(n-1)+n

print("Sum of number:",Sum(5))

#print the item of list 

fruits=["Mango","apple","banana","chikuu"]
def print_list(list,index=0):
    if(index==len(list)):
        return
    else:
        print(list[index] , end="  ") 
        print_list(list,index+1)

print_list(fruits)