#Sum of digits using recursion 
def sum_digit(n):
    if n==0:
        return 0
    return (n%10)+sum_digit(n//10)

print(sum_digit(12345))


def sum(n):
    if n==0:
        return 0
    sum=0
    while(n!=0):
        rev=n%10
        sum=sum+rev
        n=n//10
    return sum
print(sum(12345))

