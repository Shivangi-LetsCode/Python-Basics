class Account:
    interest = 3
    def __init__(self,acc,bal):
        self.acc_no = acc
        self.balance = bal

    def myFunction(self):  #instance
        self.nonstatic = 10
        #Account.nonstatic = 10  #ERROR
        print(self.nonstatic)

    @staticmethod
    def myFunction2(): #static method
         Account.static = 20 # static variable  
        #self.static = 10 #ERROR
         print(Account.static)
        

John = Account(101,50000)
John.myFunction()
# print(Account.myFunction()) #ERROR
Account.myFunction2()



'''
create a class Operations, Having 2 static methods add and sub, without
creating object of the classes display outputs.
'''










