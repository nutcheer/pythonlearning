class User():
    def __init__(self, first_name, last_name):
        self.first = first_name.title()
        self.last = last_name.title()
        self.login_attempts = 0
        
    def describe_user(self):
        print(self.first + " " + self.last)
        print(self.login_attempts)
    
    def greet_user(self):
        print("Hello " + self.first + " " + self.last + " !")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("albert", "einstein")
user.reset_login_attempts()
user.describe_user()

user.increment_login_attempts()
user.describe_user()
