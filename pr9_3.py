class User():
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
    
    def describe_user(self):
        print(self.first + " " + self.last)
    
    def greet_user(self):
        print("Hello " + self.first + " " + self.last + " !")
    
user1 = User("A", "B")
user2 = User("C", "D")
user3 = User("E", "F")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
