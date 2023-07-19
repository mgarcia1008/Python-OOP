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

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("Sorry you are already a rewards member.")
    
    def spend_points(self,amount):
        if amount < self.gold_card_points: 
            self.gold_card_points -= amount
        else:
            print("Sorry you do not have enough Gold card points to redeem this prize.")    

user_1 = User("Moira", "Rose", "mrose@sunsetbay.com", "62")
user_1.display_info()
user_1.enroll()
user_1.display_info()
user_1.spend_points(50)
user_1.display_info()
user_1.enroll() #will print out sorry you are already a rewards member after trying to re-enroll

user_2 = User("David", "Rose", "drose@roseapothecary.com", "36")
user_2.display_info()
user_2.enroll()
user_2.spend_points(80)
user_2.display_info()

user_3 = User("Alexis", "Rose", "alittlebitalexis.com", "32")
user_3.display_info()
user_3.spend_points(40) #will print out sorry message they do not have enough gold card points to redeem this prize.