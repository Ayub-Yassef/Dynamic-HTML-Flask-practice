# Creating a user class and a couple methods for an application that displays membership profiles for members of an airline's loyalty programme

class User:
    def __init__(self, first_name, surname, email, age):
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.age = age
        self.is_executive_club_member = False
        self.avios = 0
        self.tier_points = 0
    
    def display_user_info(self):
        print("++++++++++++++++++++++++")
        print(f"First Name: {self.first_name}")
        print(f"Surname: {self.surname}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Executive Club Member: {self.is_executive_club_member}")
        print(f"Avios: {self.avios}")
        print(f"Tier Points: {self.tier_points}")
        print("++++++++++++++++++++++++")
    
    def enroll(self):
        if self.is_executive_club_member:
            print("User already an Executive Club member.")
            return False
        self.is_executive_club_member = True
        self.avios = 500
    
    def spend_avios(self, amount):
        if self.avios < amount:
            print("You don't have enough Avios to complete this booking.")
            return
        self.avios -= amount


ec_user_01 = User("Yassef", "Ayub Boggeano", "ayub.yassef@test.co.uk", 34)
ec_user_01.display_user_info()
ec_user_01.enroll()
ec_user_01.display_user_info()
ec_user_01.spend_avios(150)
ec_user_01.display_user_info()
ec_user_01.spend_avios(400)
ec_user_01.display_user_info()
ec_user_01.spend_avios(300)
ec_user_01.display_user_info()