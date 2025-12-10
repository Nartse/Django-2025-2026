class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Deposit must be positive")
    def withdraw(self,amount):

        if amount<=0:
            print("Withdraw amount must be positive")
        elif self.__balance<amount:
            print("Not enough amount to withdraw")
        else:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance
acct = BankAccount(1000)
print("Initial Balance:", acct.get_balance())
acct.deposit(1000)
print("Balance after depositing 1000:", acct.get_balance())
acct.withdraw(200)
print("Balance after withdrawing 200:", acct.get_balance())
acct.withdraw(3000)
print("Balance after attempting 3000:", acct.get_balance())
acct.withdraw(-50)
print("Balance after attempting -50:", acct.get_balance())