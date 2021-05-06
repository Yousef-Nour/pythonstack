class User:
    def __init__(self,user_balance,user_name):
        self.user_balance = user_balance
        self.user_name = user_name
    def deposit(self, amount):
        self.user_balance += amount
        print(self.user_balance)
    def make_withdrawal(self, amount=0):
        if amount <= self.user_balance:
            self.user_balance -= amount
            return True
        return False
            # print(self.user_balance)
    def display_user_balance(self):
        print(self.user_name)

    def transfer_money(self, other_user, amount):
        happend = self.make_withdrawal(amount)
        if happend == True:
            other_user.deposit(amount)

anas= User(400,"Anas")
anas.make_withdrawal(100)
anas.deposit(100)
anas.display_user_balance()

yousef = User(2500, "Yousef")
print("_" * 30)
anas.display_user_balance()
yousef.display_user_balance()
print("_" * 30)
yousef.transfer_money(anas, 500)
