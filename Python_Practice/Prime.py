#Given a number, check if it is prime or not
num=int(input("Enter number: "))
is_prime=True

if num<=1:
    is_prime=False

if num>1:
    for n in range(2,num):
        if num%n==0:
            is_prime=False
            break

if(is_prime):
    print("Prime number")
else:
    print("Not prime number")