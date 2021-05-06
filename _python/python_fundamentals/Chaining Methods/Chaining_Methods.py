class User:
    def __init__(self,user_balance,user_name):
        self.user_balance = user_balance
        self.user_name = user_name

    def deposit(self, amount):
        self.user_balance += amount
        print(self.user_balance)
        return self

    def make_withdrawal(self, amount=0):
        if amount <= self.user_balance:
            self.user_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.user_name}, Balance: {self.user_balance}")
        return self

    def transfer_money(self, other_user, amount):
        happend = self.make_withdrawal(amount)
        if happend == True:
            other_user.deposit(amount)
        return self

anas= User(400,"Anas")
anas.make_withdrawal(100).deposit(100).display_user_balance()  #chain

yousef = User(2500, "Yousef")
print("_" * 30)
anas.display_user_balance()
yousef.display_user_balance()
print("_" * 30)
yousef.transfer_money(anas, 500)
yousef.transfer_money(anas, 40).display_user_balance
