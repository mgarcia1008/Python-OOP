class BankAccount:
    bank_name = "Bank of America"

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}, Current Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance 
        return self
    
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

#create two accounts
checking = BankAccount(.10, 500)
checking.deposit(500).deposit(500).deposit(500).withdraw(1000).yield_interest().display_account_info()
savings = BankAccount(.05, 1000)
savings.deposit(1000).deposit(1000).withdraw(50).withdraw(100).withdraw(25).withdraw(200).yield_interest().display_account_info()

print(BankAccount.all_balances())
