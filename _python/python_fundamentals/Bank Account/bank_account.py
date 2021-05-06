class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
                                    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance * self.int_rate + self.balance
        
        print("Sorry your balance is less than 0")
        return self

yousef = BankAccount(0.02, 1000)
khalil = BankAccount(0.03, 2000)

# yousef.display_account_info
# yousef.withdraw
# yousef.yield_interest
yousef.deposit(20).deposit(30).deposit(40).withdraw(100).yield_interest().display_account_info()
yousef.deposit(15).deposit(25).withdraw(10).withdraw(200).withdraw(150).withdraw(90).yield_interest().display_account_info()