class BankAccount:
    def __init__(self,balance):
        self.__balance = balance  # variable used to hide details # self used as a first parameter
    def deposit(self,amount):
        self.__balance +=amount
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())