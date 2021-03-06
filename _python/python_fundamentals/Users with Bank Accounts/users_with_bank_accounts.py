from bank_account import BankAccount
class User:
    def __init__(self, name, year_of_birth, balance=0, int_rate=0.01):
        self.name = name
        self.year_of_birth = year_of_birth
        self.account = BankAccount(balance=balance, int_rate=int_rate)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"{self.name} balance is: ")
        self.account.display_account_info()
        return self

    def deposit(self, amount):
    	self.account.deposit(amount)	# hmmm...the User class doesn't have an account_balance attribute anymore
        

    def transfer_money(self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.deposit(amount)
            return True
        return False
    
hani= User("hani",1992)
alaa= User("alaa",1988)

alaa.make_withdrawal(1000)
alaa.display_user_balance()

hani.transfer_money(alaa, 11000)

hani.display_user_balance()
alaa.display_user_balance()

