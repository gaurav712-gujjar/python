from abc import ABC,abstractmethod
import random
random.randint(12000387823,12000896789)

class BankAccount(ABC):
    def __init__(self,User_Name,Bank_Balance):
        self.Acc_No = random.randint(12000387823,12000896789)
        self.User_Name = User_Name
        self.Bank_Balance = Bank_Balance

    #Getter method which return private variable
    def accountBlance(self):
        return self.Bank_Balance

    def balance_update(self):
         self.Bank_Balance-= 1

    @abstractmethod
    def DepositAmount(self,amount):
        pass
        '''if amount > 0:
            self.__Bank_Balance += amount
        else:
            print("we can't deposit money")'''

    def Widrawamount(self,amount):
        if self.Bank_Balance > amount and amount > 0:
            self.Bank_Balance -= amount
        else:
            print("we can deducate money ammount")

class SavingAccount(BankAccount):
    def __init__(self,x,y):
        super().__init__(x,y)

    def DepositAmount(self,amount):
        if amount > 0:
            self.Bank_Balance += amount
        else:
            print("we can't deposit money")


    def withdraw(self,amount):  #method overidding
        if self.Bank_Balance >= amount and self.Bank_Balance - amount > 5000:
            self.Bank_Balance -= amount

        else:
            print("Minimum blance reqired is 5000")


'''b1=BankAccount("John",100)
print(b1.accountBlance())
b1.balance_update()
print(b1.accountBlance())'''
b1=SavingAccount("gaurav",1000)
b1.DepositAmount(1000)
print(b1.accountBlance())
b1.Widrawamount(1500)
print(b1.accountBlance())