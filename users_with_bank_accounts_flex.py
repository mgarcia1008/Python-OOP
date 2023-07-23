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
        if amount > self.balance:
          print("Insufficient funds: Charging a $5 fee")
          self.balance - 5
        else: 
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount) #using deposit which is calling deposit from line 11
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount) #using withdraw method/function from line 15
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s Account Balance: {self.account.balance}")
        return self


#create two accounts
checking = BankAccount(.10, 500)
checking.deposit(500).deposit(500).deposit(500).withdraw(1000).yield_interest().display_account_info()
savings = BankAccount(.05, 1000)
savings.deposit(1000).deposit(1000).withdraw(50).withdraw(100).withdraw(25).withdraw(200).yield_interest().display_account_info()

print(BankAccount.all_balances())

mindi = User("Mindi Garcia", "mgarcia@gmail.com")
peter = User("Peter Garcia", "pgarcia@gmail.com")

mindi.make_deposit(500).make_withdrawal(100).display_user_balance()
peter.make_deposit(5000).make_withdrawal(1000).display_user_balance()

