class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}\n")
        return self

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("Sorry you are already a rewards member.")
        return self
    
    def spend_points(self,amount):
        if amount < self.gold_card_points: 
            self.gold_card_points -= amount
        else:
            print("Sorry you do not have enough Gold card points to redeem this prize.")    
        return self

user_1 = User("Moira", "Rose", "mrose@sunsetbay.com", "62")
user_1.display_info().enroll().spend_points(50).display_info().enroll().display_info()


user_2 = User("David", "Rose", "drose@roseapothecary.com", "36")
user_2.display_info().enroll().spend_points(80).display_info()


user_3 = User("Alexis", "Rose", "alittlebitalexis.com", "32")
user_3.display_info().spend_points(40)
