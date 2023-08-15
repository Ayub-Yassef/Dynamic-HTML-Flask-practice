class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds, please contact us if you think this message is an error. Call Centre: 0131 556 2185")
        return self
    def display_account_info(self):
        print(f"Current balance: {self.balance}")
        return self
    def yield_int(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {}
    def open_new_account(self, int_rate=0.03, balance=0, account_type="Current"):
        new_account = BankAccount(int_rate, balance)
        self.accounts[account_type] = new_account
        return self
    def make_deposit(self, amount, account_type="Current Account"):
        self.accounts[account_type].deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self, account_type):
        print(self.name)
        self.account.display_account_info()
        return self

user1 = User("Ayub", "email@inter.net")
user1.make_deposit(400).make_deposit(1200).display_user_balance("Current Account")

user2 = User("Boggeano", "findme@web.com")
user2.make_deposit(450).display_user_balance("Current Account").make_withdrawal(460).display_user_balance("Current Account")
