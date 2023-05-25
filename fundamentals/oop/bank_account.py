class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a 5.00 GBP fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Current balance: {self.balance} GBP')
        return self
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        print(f"Your account's standing interest rate is: {self.int_rate}% - after yielded interest, your balance is {self.balance} GBP")
        return self

account1 = BankAccount(0.02, 100)
account2 = BankAccount(0.04, 0)
account1.deposit(300)
account1.deposit(300)
account1.deposit(300)
account1.withdrawal(400)
account1.withdrawal(50)
account2.deposit(100)
account2.deposit(200)
account2.withdrawal(15)
account2.withdrawal(75)
account2.withdrawal(13.25)
account2.withdrawal(44.12)
account1.yield_interest()
account2.yield_interest()
