from abc import ABC ,abstractmethod
class Account(ABC):

    @abstractmethod
    def get_balance(self):
        pass 
    @abstractmethod
    def deposit(self):
        pass
    def withdraw(self):
        pass

class Saving_account(Account):

    __balance=0
    def get_balance(self):
        return self.get_balance
    
    def deposit(self,amount):
       self.__balance+=amount
       print("Amount deposited:",amount)
    def withdraw(self,amount):
        if self.__balance<amount:
            print("Not enough balance")
            return
        self.__balance-=amount
        print("Withdraw amount:" , amount)

class Current_account(Account):
    __balance=0
    withdraw_limit=0
    def __init__(self,limit):
        self.withDraw_limit =limit

    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Amount deposited:",amount)
    def withdraw(self,amount):
        if self.__balance + self.withDraw_limit < amount:
            print("Not Enought Balance")
            return

        self.__balance -= amount
        print("Amount withdrawn :",amount)
class Bank:
    owner = "bank"
    account_number = 0
    def __init__(self,name,number,account_type= "Saving"):
        self.owner = name
        self.account_number = number

        if account_type == "Saving":
            self.account =Saving_account()
        if account_type == "Current":
            self.account =Current_account(1000)
class Manager:
    file=open("./data.txt" , "w")


    def get_customer_info(self , bank_account:Bank):
        print(f"Name : {bank_account.owner}")
        print(f"AccountNumber : {bank_account.account_number}")
        print("Account Type : ", end="")
        if(type(bank_account.account) == Saving_account):
            print("Savings Account")
        else:
            print("Current Account")
        print(f"Balance : {bank_account.account.get_balance()}")

    def __str__(self):
        return "Manager Object bro"


    



print("-----krish Account -----")
krish = Bank("krish" , 1 , "Saving")
krish.account.deposit(66)
print("*** siri Account****")
siri= Bank("siri" ,2,"Current" )
siri.account.deposit(63)


pk = Manager()
print("------ krish Account ------")
pk.get_customer_info(krish)
print("<------siri Account -------")
pk.get_customer_info(siri)
print(type(pk) == Manager)








        
        

        

