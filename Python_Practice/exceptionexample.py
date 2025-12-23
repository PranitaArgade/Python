#Write code for exception handling
try:
    a=int(input("Enter value a:"))
    b=int(input("Enter value b:"))
    print(a/b)
except ZeroDivisionError as e:
    print("number divided by zero",e)
except ValueError as e:
    print("Wrong input",e)
finally:
    print("Exception completed")