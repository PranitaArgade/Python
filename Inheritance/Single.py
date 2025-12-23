class bank:
    def __init__(self):
      bankname="UNION bank"
      print(bankname)

class Emp(bank):
    def __init__(self):
       super().__init__()
       dept="account"
       print(dept)
E=Emp()



