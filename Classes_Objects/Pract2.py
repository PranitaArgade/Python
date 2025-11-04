#create a class student and take agrument in a constructor and print aveage method
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val

        print("hii ",self.name,"your avg scord is:",sum/3)
s1=Student("Pranita Argade",[90,90,90])
s1.get_avg()

#Account
class Account:

    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    
    #Debit method
    def Debit(self,amount):
        self.balance-=amount
        print("Amount debited: ",amount)
        print("Total balance: ", self.get_balance())
    
    def Credit(self,amount):
        self.balance+=amount
        print("Credited amount: ",amount)
        print("Total balance: ",self.get_balance())
    def get_balance(self):
        return self.balance

acc=Account(1000,56789)
print(acc.balance)
print(acc.acc_no)

acc.Credit(500)
acc.Debit(200)
acc.get_balance()
    
   

    