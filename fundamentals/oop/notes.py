class LoyaltyProgramme:
    accounts = []
    def __init__(self, ratio, points):
        self.ratio = ratio
        self.points = points
        LoyaltyProgramme.accounts.append(self)
    def points_earned(self, points):
        self.points += points
        return self
    def points_spent(self, points):
        if(self.points - points) >= 0:
            self.points -= points
        else:
            print("You don't have enough Avios to complete this booking.")
        return self
    def display_membership_info(self):
        print(f"You currently have {self.points} Avios.")
        return self
    @classmethod
    def print_account_details(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = LoyaltyProgramme(ratio=1, points=0)
    def flight_completed(self, points, account="Avios"):
        self.account.points_earned(points)
        return self
    def spend_points(self, points):
        self.account.deduct(self, points)
        return self
    def display_member_accruals(self, account_type):
        print(self.name)
        self.account.display_account_info()
        return self

passenger1 = User("Yassef Ayub", "my_email@mail.net")
passenger1.flight_completed(1176)
passenger1.flight_completed(1616)
programme2 = LoyaltyProgramme(1, points=0)
passenger1.display_member_accruals("Avios")


